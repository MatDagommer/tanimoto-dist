# Use the official Miniconda image as a base
FROM continuumio/miniconda3

# Copy the environment file to the container
COPY environment.yml .

# Create a Conda environment from the environment file
RUN conda env create -f environment.yml

# Activate the Conda environment
RUN echo "source activate $(head -1 environment.yml | cut -d' ' -f2)" > ~/.bashrc
ENV PATH /opt/conda/envs/$(head -1 environment.yml | cut -d' ' -f2)/bin:$PATH

# Set the working directory
WORKDIR /app

# Copy the rest of your application code
COPY . /app

# Set the default command to run your application
CMD ["bash"]
