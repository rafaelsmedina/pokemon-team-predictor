
$(document).ready(function() {
    //load data

    $.ajax({url: "/api/pokemon/team/" + $("#team_list").text(), success: function(result){
        team = result.data

        col_size = 2

        if (team.length == 1){
            col_size = 12
        } else if (team.length == 2){
            col_size = 6

        } else if (team.length == 3){
            col_size = 4

        } else if (team.length == 4){
            col_size = 3
            
        } else if (team.length == 5){
            col_size = 15
        }
        
        var attack_data = []
        var defense_data = []
        var spattack_data = []
        var spdefense_data = []
        var speed_data = []
        var hp_data = []
        var total_data = []

        $( team ).each(function() {

            if(this["type2-image"].indexOf("nan.png") >= 0){
                type_links = "<img id=\"type1\" src=\"" + this["type1-image"] + "\">"
            } else {
                type_links = "<img id=\"type1\" src=\"" + this["type1-image"] + "\">" + "<img id=\"type2\" src=\"" + this["type2-image"] + "\">"
            }

            $("#team-div").append(
                "<div class=\"col-md-" + col_size + "\" id=\"poke-id\">" + 
                "<img id=\"image-link\" src=\"" + this["img-link"] + "\">" +
                "<h5 id=\"pkmn-name\">" + "<small> #" + this.num_dex + " </small>" + this.forme + "</h5>" +
                type_links +
                "</div>");

            n = this.num_dex.toString();
            attack_data.push({"name": this.forme, "value": this.attack, "dex": this.num_dex})
            defense_data.push({"name": this.forme, "value": this.defense})
            spattack_data.push({"name": this.forme, "value": this.spattack})
            spdefense_data.push({"name": this.forme, "value": this.spdefense})
            speed_data.push({"name": this.forme, "value": this.speed})
            hp_data.push({"name": this.forme, "value": this.hp})
            total_data.push({"name": this.forme, "value": this.total})
        });

        //attack graph
          var visualization = d3plus.viz()
            .container("#attack_viz")
            .data(attack_data)
            .type("bar")
            .id("name")
            .x("name")
            .y("value")
            .title("Attack")
            .draw();

        //defense graph
          var visualization = d3plus.viz()
            .container("#defense_viz")
            .data(defense_data)
            .type("bar")
            .id("name")
            .x("name")
            .y("value")
            .title("Defense")
            .draw();

        //spattack graph
          var visualization = d3plus.viz()
            .container("#spattack_viz")
            .data(spattack_data)
            .type("bar")
            .id("name")
            .x("name")
            .y("value")
            .title("SP. Attack")
            .draw();

        //spdefense graph
          var visualization = d3plus.viz()
            .container("#spdefense_viz")
            .data(spdefense_data)
            .type("bar")
            .id("name")
            .x("name")
            .y("value")
            .title("Sp. Defense")
            .draw();

        //speed graph
          var visualization = d3plus.viz()
            .container("#speed_viz")
            .data(speed_data)
            .type("bar")
            .id("name")
            .x("name")
            .y("value")
            .title("Speed")
            .draw();

        //hp graph
          var visualization = d3plus.viz()
            .container("#hp_viz")
            .data(hp_data)
            .type("bar")
            .id("name")
            .x("name")
            .y("value")
            .title("HP")
            .draw();

        //total graph
          var visualization = d3plus.viz()
            .container("#total_viz")
            .data(total_data)
            .type("bar")
            .id("name")
            .x("name")
            .y("value")
            .title("Total")
            .draw();
        
    }});
});
