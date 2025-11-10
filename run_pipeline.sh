#!/bin/bash

# run_pipeline.sh
# Script to run the job matching pipeline with cover letter generation

echo "AI Job Agent - Running pipeline with cover letter generation"
echo "========================================================="

# Default values
QUERY="data analyst"
LOCATION=""

# Parse command line arguments if provided
if [ $# -ge 1 ]; then
    QUERY="$1"
fi

if [ $# -ge 2 ]; then
    LOCATION="$2"
fi

echo "Search query: $QUERY"
echo "Location: ${LOCATION:-any}"
echo "---------------------------------------------------------"

# Run pipeline with cover letter generation enabled
python run_with_covers.py

echo "========================================================="
echo "Pipeline completed. Check outputs/ directory for results."