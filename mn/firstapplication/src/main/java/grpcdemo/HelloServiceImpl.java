package grpcdemo;

import io.grpc.stub.StreamObserver;

public class HelloServiceImpl extends FirstapplicationServiceGrpc.FirstapplicationServiceImplBase {

    @Override
    public void send(
            FirstapplicationRequest request, StreamObserver<FirstapplicationReply> responseObserver) {

        String greeting = new StringBuilder()
                .append("Hello, ")
                .append(request.getFirstName())
                .append(" ")
                .append(request.getLastName())
                .toString();

        FirstapplicationReply response = FirstapplicationReply.newBuilder()
                .setGreeting(greeting)
                .build();

        responseObserver.onNext(response);
        responseObserver.onCompleted();
    }
}
