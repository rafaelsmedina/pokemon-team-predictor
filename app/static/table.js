$(document).ready(function() {
    $('#list-pokemon').DataTable( {
        "ajax": "/api/pokemon",
            "columns": [
                {"data" : "num_dex" },
                {"data" : "species" },
                {"data" : "forme" },
                {"data" : "type1" },
                {"data" : "type2" },
                {"data" : "ability1" },
                {"data" : "ability2" },
                {"data" : "abilityH" },
                {"data" : "hp" },
                {"data" : "attack" },
                {"data" : "defense" },
                {"data" : "spattack" },
                {"data" : "spdefense" },
                {"data" : "speed" },
                {"data" : "total" },
                {"data" : "pkmn_class" },
                {"data" : "percent_male" },
                {"data" : "percent_female" },

            ]
    });
});