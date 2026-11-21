# Capacity estimate
150,000 students / 7,200 seconds = **20.83 average logins per second**.
Required replicas = ceil((20.83 × burst factor × safety factor) / measured complete-login RPS per replica).
Illustration only: if one replica sustains 12 login transactions/s, burst factor=3 and safety factor=1.5, replicas=ceil((20.83×3×1.5)/12)=8. Replace 12 with your measured complete-login throughput. A homepage GET test is not a complete login transaction. Include database, cache, authentication, network and failure reserve.
