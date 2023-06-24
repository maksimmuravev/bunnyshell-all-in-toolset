use std::env;
use std::fs::File;
use std::io::{self, BufRead};
use sentry::{ClientOptions, Level};
use sentry::protocol::Event;
use sentry::types::Dsn;

fn main() {
    // Initialize the Sentry client
    let mut options = ClientOptions::new();
    options.dsn = env::var("SENTRY_DSN").ok().and_then(|dsn_string| dsn_string.parse::<Dsn>().ok());
    options.debug = true; // Enable debug logging
    let _sentry = sentry::init(options);

    // Read data from file and process it
    if let Err(err) = process_file("data.txt") {
        // Capture and send the error to Sentry
        let mut event = Event::new();
        event.level = Level::Error;
        event.message = Some(err.to_string());
        sentry::capture_event(event);
        println!("Exception sent to Sentry!");
    } else {
        println!("File processed successfully!");
    }
}

fn process_file(filename: &str) -> Result<(), Box<dyn std::error::Error>> {
    let file = File::open(filename)?;
    let reader = io::BufReader::new(file);

    for line in reader.lines() {
        let line = line?;
        // Process the data from each line
        process_data(&line)?;
    }

    Ok(())
}

fn process_data(data: &str) -> Result<(), Box<dyn std::error::Error>> {
    // Business logic code to process the data
    // Replace this with your actual data processing logic
    println!("Data processed: {}", data);
    Ok(())
}

