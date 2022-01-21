# quarkus-example
![Build](https://github.com/gregwhitaker/quarkus-example/workflows/Build/badge.svg)

Simple example of a web service implemented with [Quarkus](http://quarkus.io).

This example shows you how to build and compile a simple "Hello World" RESTful webservice using Quarkus, GraalVM, and Gradle.

## Prerequisites
This example requires that you have the [GraalVM installed](https://github.com/oracle/graal/releases/tag/vm-19.2.1) on your development machine. 

**Note:** As of the time of this example Quarkus only supports GraalVM version `19.2.1`. Please refer to the [Quarkus](http://quarkus.io) website for information
on current GraalVM compatibility.

## Building the Example
Run the following command to build example:

    ./gradlew clean build
        
This will build the example as both an executable JAR and a native image using GraalVM.

For more detailed information check out the [Building Quarkus Apps with Gradle](https://quarkus.io/guides/gradle-tooling) documentation on the Quarkus website.

## Running the Example
Follow the steps below to run the example application:

1. Run the following commands to start the native image version of the application:

        cd build
        ./quarkus-example-0.1.0-runner
        
    If successful, you will see the following in the terminal:
    
        2019-12-04 15:23:59,587 INFO  [io.quarkus] (main) quarkus-example 0.1.0 (running on Quarkus 1.0.1.Final) started in 0.009s. Listening on: http://0.0.0.0:8080
        2019-12-04 15:23:59,587 INFO  [io.quarkus] (main) Profile prod activated.
        2019-12-04 15:23:59,587 INFO  [io.quarkus] (main) Installed features: [cdi, resteasy, resteasy-jackson]

2. In a new terminal, run the following command to send an HTTP request to the service:

        curl http://localhost:8080/hello?name=Bob
    
    If successful, you will see a response similar to the following in the terminal:
    
        {"create_time":"2019-12-04 03:24:56","message":"Hello, Bob!"}

## Bugs and Feedback
For bugs, questions, and discussions please use the [Github Issues](https://github.com/gregwhitaker/quarkus-example/issues).

## License
MIT License

Copyright (c) 2019 Greg Whitaker

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
