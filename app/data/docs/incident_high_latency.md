# Incident Report: High Latency Event

## Summary
On 2025-01-12, multiple services experienced elevated response times
due to increased database latency.

## Impact
- API response times increased by 3x
- Approximately 15% of requests timed out
- SLA breach for premium customers

## Root Cause
A sudden traffic surge caused connection pool exhaustion in the primary database.
Autoscaling was delayed due to misconfigured thresholds.

## Resolution
- Increased database connection limits
- Manually scaled application instances
- Updated autoscaling policies

## Lessons Learned
- Review autoscaling thresholds quarterly
- Add alerts for database connection saturation

