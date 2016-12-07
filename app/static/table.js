$(document).ready(function() {
    $('#list-pokemon').DataTable( {
        "ajax": "/api/pokemon",
            "columns": [
                {"data" : "num_dex" },
                {
                    "data" : "forme",
                    "render" : function (data, type, full, meta) {
                        return '<a href="/pokemon/'+full.id+'">'+data+'</a>'
                    }
                },
                {
                    "data" : "id",
                    "visible": false,
                    "searchable": false
                }
            ]
    });
});