# Use the latest Alpine image as the base image
FROM alpine:latest

# Install Docker inside the container to allow Docker commands
RUN apk add --no-cache docker

# Copy the entrypoint script into the container
COPY entrypoint.sh /entrypoint.sh

# Make sure the entrypoint script is executable
RUN chmod +x /entrypoint.sh

# Set the entrypoint to run the script
ENTRYPOINT ["/entrypoint.sh"]

# Expose necessary ports for your reverse proxy if needed (adjust according to your app)
EXPOSE 80 443
