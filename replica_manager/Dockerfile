FROM alpine:latest

# Install Docker inside the container so we can run 'docker run' commands
RUN apk add --no-cache docker

# Copy the entrypoint script into the container
COPY entrypoint.sh /entrypoint.sh

# Make it executable
RUN chmod +x /entrypoint.sh

# Set the entrypoint to run the script
ENTRYPOINT ["/entrypoint.sh"]
