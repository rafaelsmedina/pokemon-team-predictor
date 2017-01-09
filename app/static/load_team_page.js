
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

        var i = 1;

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
            attack_data.push({"name": this.forme, "value": this.attack, "skill": "attack", "num" :"slot" + i.toString()})
            defense_data.push({"name": this.forme, "value": this.defense, "skill": "defense", "num" :"slot" + i.toString()})
            spattack_data.push({"name": this.forme, "value": this.spattack, "skill": "spattack", "num" :"slot" + i.toString()})
            spdefense_data.push({"name": this.forme, "value": this.spdefense, "skill": "spdefense", "num" :"slot" + i.toString()})
            speed_data.push({"name": this.forme, "value": this.speed, "skill": "speed", "num" :"slot" + i.toString()})
            hp_data.push({"name": this.forme, "value": this.hp, "skill": "hp", "num" :"slot" + i.toString()})
            total_data.push({"name": this.forme, "value": this.total, "skill": "total", "num" :"slot" + i.toString()})

            i = i + 1;
        });

        var attributes = {
            "slot1": "#FF5B2F",
            "slot2": "#26CC6E",    
            "slot3": "#FFAE2F",
            "slot4": "#B4F42D",
            "slot5": "#DB2991",
            "slot6": "#3173C2"
          }

        //attack graph
        var max = d3.max(attack_data, function(d) { return +d.value;});
          var visualization = d3plus.viz()
            .container("#attack_viz")
            .data(attack_data)
            .type("bar")
            .id("name")
            .x("skill")
            .x({"label": false, "padding": 1, "grid": false, "ticks": { "color": "#fff", "labels":  false }})
            .y("value")
            .y({"range": [0, max]})
            .title("Attack")
            .attrs(attributes)
            .color(function(d){
                console.log(d.num)
                console.log(attributes[d.num])
              return attributes[d.num];
            })
            .legend(false)
            .draw();

        //defense graph
        max = d3.max(defense_data, function(d) { return +d.value;});
          var visualization = d3plus.viz()
            .container("#defense_viz")
            .data(defense_data)
            .type("bar")
            .id("name")
            .x("skill")
            .x({"label": false, "padding": 1, "grid": false, "ticks": { "color": "#fff", "labels":  false }})
            .y("value")
            .y({"range": [0, max]})
            .title("Defense")
            .attrs(attributes)
            .color(function(d){
                console.log(d.num)
                console.log(attributes[d.num])
              return attributes[d.num];
            })
            .legend(false)
            .draw();

        //spattack graph
        max = d3.max(spattack_data, function(d) { return +d.value;});
          var visualization = d3plus.viz()
            .container("#spattack_viz")
            .data(spattack_data)
            .type("bar")
            .id("name")
            .x("skill")
            .x({"label": false, "padding": 1, "grid": false, "ticks": { "color": "#fff", "labels":  false }})
            .y("value")
            .y({"range": [0, max]})
            .title("SP. Attack")
            .attrs(attributes)
            .color(function(d){
                console.log(d.num)
                console.log(attributes[d.num])
              return attributes[d.num];
            })
            .legend(false)
            .draw();

        //spdefense graph
        max = d3.max(spdefense_data, function(d) { return +d.value;});
          var visualization = d3plus.viz()
            .container("#spdefense_viz")
            .data(spdefense_data)
            .type("bar")
            .id("name")
            .x("skill")
            .x({"label": false, "padding": 1, "grid": false, "ticks": { "color": "#fff", "labels":  false }})
            .y("value")
            .y({"range": [0, max]})
            .title("Sp. Defense")
            .attrs(attributes)
            .color(function(d){
                console.log(d.num)
                console.log(attributes[d.num])
              return attributes[d.num];
            })
            .legend(false)
            .draw();

        //speed graph
        max = d3.max(speed_data, function(d) { return +d.value;});
          var visualization = d3plus.viz()
            .container("#speed_viz")
            .data(speed_data)
            .type("bar")
            .id("name")
            .x("skill")
            .x({"label": false, "padding": 1, "grid": false, "ticks": { "color": "#fff", "labels":  false }})
            .y("value")
            .y({"range": [0, max]})
            .title("Speed")
            .attrs(attributes)
            .color(function(d){
                console.log(d.num)
                console.log(attributes[d.num])
              return attributes[d.num];
            })
            .legend(false)
            .draw();

        //hp graph
        max = d3.max(hp_data, function(d) { return +d.value;});
          var visualization = d3plus.viz()
            .container("#hp_viz")
            .data(hp_data)
            .type("bar")
            .id("name")
            .x("skill")
            .x({"label": false, "padding": 1, "grid": false, "ticks": { "color": "#fff", "labels":  false }})
            .y("value")
            .y({"range": [0, max]})
            .title("HP")
            .attrs(attributes)
            .color(function(d){
                console.log(d.num)
                console.log(attributes[d.num])
              return attributes[d.num];
            })
            .legend(false)
            .draw();

        //total graph
        max = d3.max(total_data, function(d) { return +d.value;});
          var visualization = d3plus.viz()
            .container("#total_viz")
            .data(total_data)
            .type("bar")
            .id("name")
            .x("skill")
            .x({"label": false, "padding": 1, "grid": false, "ticks": { "color": "#fff", "labels":  false }})
            .y("value")
            .y({"range": [0, max]})
            .title("Total")
            .attrs(attributes)
            .color(function(d){
                console.log(d.num)
                console.log(attributes[d.num])
              return attributes[d.num];
            })
            .legend(false)
            .draw();
        
    }});
});
