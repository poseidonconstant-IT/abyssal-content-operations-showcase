# Architecture notes

## Release schedule

The production workflow prepares content at 05:30, 11:30, and 17:30 ICT for
scheduled release windows at 06:00, 12:00, and 18:00 ICT. Each release passes
through a HOLD window for human review.

## Delivery contract

Each platform is recorded independently. A delivery is successful only for the
specific destination that confirms publication. If one destination fails, retry
state contains that destination only; already successful destinations are not
duplicated.

## Portfolio boundary

The public case study exposes architecture and safe UI code only. The production
application, runtime data, credential configuration, and operational dashboards
remain private.
