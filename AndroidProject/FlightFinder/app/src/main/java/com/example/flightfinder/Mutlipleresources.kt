package com.example.flightfinder

import com.google.gson.annotations.SerializedName


class MultipleResource {
    @SerializedName("page")
    var page: Int? = null

    @SerializedName("per_page")
    var perPage: Int? = null

    @SerializedName("total")
    var total: Int? = null

    @SerializedName("total_pages")
    var totalPages: Int? = null

    @SerializedName("data")
    var data: List<Datum>? = null

    inner class Datum {
        @SerializedName("id")
        var id: Int? = null

        @SerializedName("name")
        var name: String? = null

        @SerializedName("year")
        var year: Int? = null

        @SerializedName("pantone_value")
        var pantoneValue: String? = null
    }
}