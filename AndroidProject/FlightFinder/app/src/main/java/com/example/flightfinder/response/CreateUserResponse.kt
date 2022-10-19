package com.example.flightfinder.response

import com.google.gson.annotations.SerializedName


class CreateUserResponse {
    @SerializedName("name")
    var name: String? = null

    @SerializedName("job")
    var job: String? = null

    @SerializedName("id")
    var id: String? = null

    @SerializedName("createdAt")
    var createdAt: String? = null
}