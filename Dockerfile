FROM python:3.11-slim-bookworm
# Set the working directory
WORKDIR /app

# Install necessary dependencies
RUN apt-get update \
    && apt-get install -y libgl1 libglib2.0-0 curl wget git procps \
    && apt-get clean

ENV GIT_SSH_COMMAND="ssh -o StrictHostKeyChecking=no"

# This will install torch with *only* cpu support
# Remove the --extra-index-url part if you want to install all the gpu requirements
# For more details in the different torch distribution visit https://pytorch.org/.
RUN pip3 install --no-cache-dir docling --extra-index-url https://download.pytorch.org/whl/cpu

ENV HF_HOME=/tmp/
ENV TORCH_HOME=/tmp/

RUN docling-tools models download

# Copy the requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# On container environments, always set a thread budget to avoid undesired thread congestion.
ENV OMP_NUM_THREADS=4

# Copy the source code
COPY src/ ./src/

# Expose the port
EXPOSE $PORT

# Command to run the application
CMD ["python3", "src/app.py"]
