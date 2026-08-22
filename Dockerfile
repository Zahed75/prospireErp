FROM python:3.12-slim-bookworm

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libxml2-dev \
    libxslt1-dev \
    libldap2-dev \
    libsasl2-dev \
    libpq-dev \
    libcairo2-dev \
    pkg-config \
    postgresql-client \
    curl \
    ca-certificates \
    node-less \
    git \
    xz-utils \
    fonts-noto-core \
    fonts-noto-cjk \
    fonts-noto-color-emoji \
    # Install official wkhtmltopdf with patched Qt.
    # There is no official bookworm .deb; the Ubuntu 22.04 (jammy) build
    # links against libssl3 and installs cleanly on Debian bookworm.
    && curl -fsSL -o /tmp/wkhtmltox.deb \
       https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6.1-2/wkhtmltox_0.12.6.1-2.jammy_amd64.deb \
    && apt-get install -y --no-install-recommends /tmp/wkhtmltox.deb \
    && rm -f /tmp/wkhtmltox.deb \
    && rm -rf /var/lib/apt/lists/*

# Create odoo user
RUN useradd -m -d /opt/odoo -s /bin/bash odoo

# Set working directory
WORKDIR /opt/odoo

# Copy requirements first for better caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all application files
COPY . .

# Setup directories and permissions
RUN mkdir -p /var/lib/odoo /var/log/odoo && \
    chown -R odoo:odoo /var/lib/odoo /var/log/odoo /opt/odoo

# Make entrypoint and odoo-bin executable
RUN chmod +x /opt/odoo/entrypoint.sh /opt/odoo/odoo-bin

# Switch to odoo user
USER odoo

# Expose Odoo ports
EXPOSE 8069 8072

# Entrypoint script
ENTRYPOINT ["/opt/odoo/entrypoint.sh"]

# Run Odoo
CMD /opt/odoo/odoo-bin -c /opt/odoo/odoo.conf -d "${DB_NAME:-prospire_hq}" --data-dir /var/lib/odoo