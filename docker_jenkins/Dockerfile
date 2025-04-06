FROM jenkins/jenkins:latest

# Switch to root user for administrative tasks
USER root

# Update package list and install required system dependencies
RUN apt-get update && apt-get install -y \
    sudo \
    git \
    curl \
    vim \
    python3 \
    python3-pip \
    python3-venv \
    && rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get install -y \
    unixodbc \
    unixodbc-dev \
    freetds-dev \
    freetds-bin \
    tdsodbc \
    gnupg \
&& rm -rf /var/lib/apt/lists/*

# Microsoft ODBC driver install
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
&& curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list \
&& apt-get update \
&& ACCEPT_EULA=Y apt-get install -y msodbcsql17

# Add Jenkins user to sudoers for privileged operations
RUN echo "jenkins ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

# Create a Python virtual environment and install Python dependencies
RUN python3 -m venv /opt/venv && \
    /opt/venv/bin/pip install --no-cache-dir pytest pytest-html pyodbc regex

# Set PATH environment variable to include the virtual environment binaries
ENV PATH="/opt/venv/bin:$PATH"

# Change ownership of the venv directory to the Jenkins user for proper access
RUN chown -R jenkins:jenkins /opt/venv

# Switch back to Jenkins user for security and non-root best practices
USER jenkins

# Expose Jenkins standard HTTP and JNLP agent communication ports
EXPOSE 8080 50000

# Define the default command to start Jenkins
CMD ["/usr/bin/tini", "--", "/usr/local/bin/jenkins.sh"]
