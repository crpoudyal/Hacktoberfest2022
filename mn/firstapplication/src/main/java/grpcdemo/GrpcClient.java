package grpcdemo;

import io.grpc.ManagedChannel;
import io.grpc.ManagedChannelBuilder;

public class GrpcClient {
    public static void main(String[] args) {
        ManagedChannel channel = ManagedChannelBuilder.forAddress("localhost", 8080)
                .usePlaintext()
                .build();

        FirstapplicationServiceGrpc.FirstapplicationServiceBlockingStub stub
                = FirstapplicationServiceGrpc.newBlockingStub(channel);

        FirstapplicationReply helloResponse = stub.send(FirstapplicationRequest.newBuilder()
                .setFirstName("Baeldung")
                .setLastName("gRPC")
                .build());

        channel.shutdown();
    }
}
