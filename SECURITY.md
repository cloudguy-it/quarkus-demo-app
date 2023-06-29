# Security Policy

## Supported Versions

Use this section to tell people about which versions of your project are
currently being supported with security updates.

| Vulnerability ID | Package Name                                | Installed Version | Fixed Version              | Title                                                                                                  | Severity |
|------------------|---------------------------------------------|-------------------|----------------------------|--------------------------------------------------------------------------------------------------------|----------|
| CVE-2020-36518   | com.fasterxml.jackson.core:jackson-databind | 2.11.3            | 2.12.6.1, 2.13.2.1         | denial of service via a large depth of nested objects                                                  | HIGH     |
| CVE-2021-46877   | com.fasterxml.jackson.core:jackson-databind | 2.11.3            | 2.12.6, 2.13.1             | Possible DoS if using JDK serialization to serialize JsonNode                                          | HIGH     |
| CVE-2022-42003   | com.fasterxml.jackson.core:jackson-databind | 2.11.3            | 2.12.7.1, 2.13.4.1         | deep wrapper array nesting wrt UNWRAP_SINGLE_VALUE_ARRAYS                                              | HIGH     |
| CVE-2022-42004   | com.fasterxml.jackson.core:jackson-databind | 2.11.3            | 2.12.7.1, 2.13.4           | use of deeply nested arrays                                                                            | HIGH     |
| CVE-2021-23463   | com.h2database:h2                           | 1.4.197           | 2.0.202                    | h2database: XXE injection vulnerability                                                                | CRITICAL |
| CVE-2021-42392   | com.h2database:h2                           | 1.4.197           | 2.0.206                    | h2: Remote Code Execution in Console                                                                   | CRITICAL |
| CVE-2022-23221   | com.h2database:h2                           | 1.4.197           | 2.1.210                    | h2: Loading of custom classes from remote servers through JNDI                                         | CRITICAL |
| CVE-2021-37136   | io.netty:netty-codec                        | 4.1.49.Final      | 4.1.68                     | Bzip2Decoder doesn't allow setting size restrictions for decompressed data                             | HIGH     |
| CVE-2021-37137   | io.netty:netty-codec                        | 4.1.49.Final      | 4.1.68                     | SnappyFrameDecoder doesn't restrict chunk length and may buffer skippable chunks in an unnecessary way | HIGH     |
| CVE-2022-4147    | io.quarkus:quarkus-vertx-http               | 1.10.2.Final      | 2.13.5.Final, 2.14.2.Final | quarkus-vertx-http: Security misconfiguration of CORS : OWASP A05_2021 level in Quarkus                | HIGH     |

## Reporting a Vulnerability

Use this section to tell people how to report a vulnerability.

Tell them where to go, how often they can expect to get an update on a
reported vulnerability, what to expect if the vulnerability is accepted or
declined, etc.
