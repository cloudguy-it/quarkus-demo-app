# Quarkus playground

[![CircleCI](https://circleci.com/gh/DonaldLika/quarkus-playground.svg?style=shield&circle-token=e8f15aad92244e14d81e773e17af4dfcd4d587f)](https://github.com/DonaldLika/quarkus-playground)
[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

This codebase was created to demonstrate a fully fledged fullstack application built with [Quarkus](https://quarkus.io/) including CRUD operations, authentication, routing, pagination, and more.

# How it works

This application basicaly uses Quarkus Framework with Java 8 with some other modules known to development community:

* Hibernate 5
* Jackson for JSON
* H2 in memory database
* JPA Criteria

# Getting started

### Start local server

```bash
 ./gradlew quarkusDev
 ```
The server should be running at http://localhost:8080

### Running the application tests

``` 
 ./gradlew test
```

## Packaging and running the application

The application can be packaged using:
```shell script
./gradlew build
```
It produces the `quarkus-playground-1.0.0-SNAPSHOT-runner.jar` file in the `/build` directory.
Be aware that it’s not an _über-jar_ as the dependencies are copied into the `build/lib` directory.

If you want to build an _über-jar_, execute the following command:
```shell script
./gradlew build -Dquarkus.package.type=uber-jar
```

The application is now runnable using `java -jar build/quarkus-playground-1.0.0-SNAPSHOT-runner.jar`.

### Building native executable

You can create a native executable using: 
```shell script
./gradlew build -Dquarkus.package.type=native
```

Or, if you don't have GraalVM installed, you can run the native executable build in a container using: 
```shell script
./gradlew build -Dquarkus.package.type=native -Dquarkus.native.container-build=true
```

You can then execute your native executable with: `./build/quarkus-playground-1.0.0-SNAPSHOT-runner`

If you want to learn more about building native executables, please consult https://quarkus.io/guides/gradle-tooling.

## Help

Improvements are welcome, feel free to contribute.
