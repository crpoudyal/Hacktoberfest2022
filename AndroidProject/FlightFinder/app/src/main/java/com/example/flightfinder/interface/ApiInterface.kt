package com.example.flightfinder

import com.example.flightfinder.model.User
import com.example.flightfinder.model.UserList
import retrofit2.Call
import retrofit2.http.*

interface ApiInterface {
    @GET("/api/unknown")
    fun doGetListResources(): Call<MultipleResource?>?

    @POST("/api/users")
    fun createUser(@Body user: User?): Call<User?>?

    @GET("/api/users?")
    fun doGetUserList(@Query("page") page: String?): Call<UserList?>?

    @FormUrlEncoded
    @POST("/api/users?")
    fun doCreateUserWithField(
        @Field("name") name: String?,
        @Field("job") job: String?
    ): Call<UserList?>?
}