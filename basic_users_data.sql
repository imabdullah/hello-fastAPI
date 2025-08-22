-- Create database (if not exists)
CREATE DATABASE IF NOT EXISTS fastapi_db;
USE fastapi_db;

-- Drop table if exists (for testing purposes)
-- DROP TABLE IF EXISTS users;

-- Create users table
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    username VARCHAR(100) NOT NULL UNIQUE,
    full_name VARCHAR(255) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,

    -- Add indexes for better performance
    INDEX idx_email (email),
    INDEX idx_username (username),
    INDEX idx_is_active (is_active),
    INDEX idx_created_at (created_at)
);

-- Insert sample data
INSERT INTO users (email, username, full_name, is_active) VALUES
('john.doe@example.com', 'johndoe', 'John Doe', TRUE),
('jane.smith@example.com', 'janesmith', 'Jane Smith', TRUE),
('mike.johnson@example.com', 'mikej', 'Mike Johnson', TRUE),
('sarah.wilson@example.com', 'sarahw', 'Sarah Wilson', FALSE),
('david.brown@example.com', 'davidb', 'David Brown', TRUE),
('lisa.garcia@example.com', 'lisag', 'Lisa Garcia', TRUE),
('tom.anderson@example.com', 'toma', 'Tom Anderson', TRUE),
('amy.taylor@example.com', 'amyt', 'Amy Taylor', FALSE),
('robert.lee@example.com', 'robertlee', 'Robert Lee', TRUE),
('emma.davis@example.com', 'emmad', 'Emma Davis', TRUE);

-- Verify the data
SELECT * FROM users;

-- Check table structure
DESCRIBE users;

-- Get user count
SELECT COUNT(*) as total_users FROM users;

-- Get active users only
SELECT * FROM users WHERE is_active = TRUE;

-- Get users created in the last hour (useful for testing)
SELECT * FROM users WHERE created_at >= DATE_SUB(NOW(), INTERVAL 1 HOUR);