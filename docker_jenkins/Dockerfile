# Start with the latest Jenkins image
FROM jenkins/jenkins:latest

# --- Switch to root user for administrative tasks ---
USER root

# --- Install dependencies and Microsoft SQL Server ODBC Driver ---
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - && \
    curl https://packages.microsoft.com/config/debian/11/prod.list > /etc/apt/sources.list.d/mssql-release.list && \
    apt-get update && apt-get install -y \
    sudo \
    git \
    curl \
    vim \
    python3 \
    python3-pip \
    python3-venv \
    unixodbc \
    unixodbc-dev \
    libgssapi-krb5-2 \
    apt-transport-https \
    software-properties-common && \
    ACCEPT_EULA=Y apt-get install -y msodbcsql17 && \
    rm -rf /var/lib/apt/lists/* && \
    echo "jenkins ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers && \
    python3 -m venv /opt/venv && \
    /opt/venv/bin/pip install --no-cache-dir \
    pytest pytest-html pyodbc regex && \
    rm -rf /root/.cache/pip && \
    chown -R jenkins:jenkins /opt/venv

# --- Set environment variables and switch back to Jenkins user ---
ENV PATH="/opt/venv/bin:$PATH"
ENV DOCKERHOST="dockerhost"

USER jenkins

# --- Expose Jenkins standard HTTP and JNLP agent communication ports ---
EXPOSE 8080 50000

# --- Allow testing or debugging via direct shell command ---
CMD ["bash"]
