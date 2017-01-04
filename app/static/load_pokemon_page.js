
$(document).ready(function() {
    //load data
    $.ajax({url: "/api/pokemon/" + $("#forme-title").text(), success: function(result){
        pokemon = JSON.parse(result.data)

        $("#forme-title").text(pokemon["forme"]);
        $("#forme-header").html('<small> #' + pokemon["num_dex"] + ' </small>' + pokemon["forme"]);

        //fill abilities

        if((pokemon["ability2"] == 'nan') || (pokemon["ability1"] == pokemon["ability2"]) ){
            $("#a1-li").text(pokemon["ability1"]);
            $("#ability1-li").text(pokemon["ability1-desc"]);
            $("#ab-2").hide();
            $("#a2-li").hide();
            $("#ability2-li").hide()
        }
        else {
            $("#a1-li").text(pokemon["ability1"]);
            $("#ability1-li").text(pokemon["ability1-desc"]);
            $("#a2-li").text(pokemon["ability2"]);
            $("#ability2-li").text(pokemon["ability2-desc"]);
        }
        if(pokemon["abilityH"] != 'nan'){
            $("#aH-li").text('Hidden: ' + pokemon["abilityH"]);
            $("#abilityH-li").text(pokemon["abilityH-desc"]);
        } else {
            $("#ab-H").hide();
            $("#aH-li").hide();
            $("#abilityH-li").hide();
        } 

        //fill stats
        $("#hp-li").text(pokemon["hp"]);
        $("#attack-li").text(pokemon["attack"]);
        $("#defense-li").text(pokemon["defense"]);
        $("#spattack-li").text(pokemon["spattack"]);
        $("#spdefense-li").text(pokemon["spdefense"]);
        $("#speed-li").text(pokemon["speed"]);
        $("#total-li").text(pokemon["total"]);

        //more info
        $("#weight-li").text(pokemon["weight"]);
        $("#height-li").text(pokemon["height"]);

        if(pokemon["dex2"] == 'nan'){
            $("#dex-entrances-tab").hide();
            $("#dex-entrances-li").hide();
        }
        else {
            $("#dex1-li").text(pokemon["dex1"]);
            $("#dex2-li").text(pokemon["dex2"]);}

        $("#class-li").text(pokemon["pkmn_class"]);

        if(pokemon["pre_evolution"] == 'nan'){
            $("#pre-ev-li").text("-");            
        }
        else {
            $("#pre-ev-li").text(pokemon["pre_evolution"]);
        }

        if(pokemon["egg_group2"] == 'nan'){
            $("#egg1-li").text(pokemon["egg_group1"]);
            $("#egg2-li").text("-");
        }
        else {
            $("#egg1-li").text(pokemon["egg_group1"]);
            $("#egg2-li").text(pokemon["egg_group2"]);
        }


        // images links
        $("#image-link").attr("src", pokemon["img-link"]);

        if(pokemon["type2-image"].indexOf("nan.png") >= 0){
            $("#type1").attr("src", pokemon["type1-image"]);
            $("#type2").hide();
        } else {
            $("#type1").attr("src", pokemon["type1-image"]);
            $("#type2").attr("src", pokemon["type2-image"]);
        }

        //stats graph
        var stats_data = [
            {"name": pokemon["forme"] ,"skill": "HP", "value": pokemon["hp"] , "type": pokemon["type1"] },
            {"name": pokemon["forme"] ,"skill": "Attack", "value": pokemon["attack"] , "type": pokemon["type1"] },
            {"name": pokemon["forme"] ,"skill": "Defense", "value": pokemon["defense"] , "type": pokemon["type1"] },
            {"name": pokemon["forme"] ,"skill": "Sp. Attack", "value": pokemon["spattack"] , "type": pokemon["type1"] },
            {"name": pokemon["forme"] ,"skill": "Sp. Defense", "value": pokemon["spdefense"] , "type": pokemon["type1"] },
            {"name": pokemon["forme"] ,"skill": "Speed", "value": pokemon["speed"] , "type": pokemon["type1"] }
          ];

            var attributes = {
            "Normal": "#A8A878",
            "Flying": "#A890F0",    
            "Poison": "#A040A0",
            "Fighting": "#C03028",
            "Fire": "#F08030",
            "Water": "#6890F0",    
            "Ice": "#98D8D8",
            "Fairy": "#EE99AC",
            "Ghost": "#705898",
            "Ground": "#E0C068",    
            "Rock": "#B8A038",
            "Electric": "#F8D030",
            "Dragon": "#7038F8",
            "Dark": "#705848",    
            "Steel": "#B8B8D0",
            "Grass": "#78C850",
            "Bug": "#A8B820",
            "Psychic": "#F85888"
          }

          var visualization = d3plus.viz()
            .container("#stats_viz")
            .data(stats_data)
            .id(["name", "skill"])
            .size("value")
            .type("radar")
            .attrs(attributes)
            .color(function(d){
              return attributes[d.type];
            })  
            .draw();

        //GENDER VISUALIZATION
        var data = [
            {"gender": "Female", "value": pokemon["percent_female"]},
            {"gender" : "Male", "value": pokemon["percent_male"]}
            ];

            if (pokemon["percent_male"] == 0 && pokemon["percent_female"] == 0){
                data = [{"name": pokemon["forme"], "gender": "Genderless", "value": 100}]
            } 

        var gender_colours = {
            "Female": "#f8c2f9",
            "Male": "#bdd5fc",    
            "Genderless": "#ae76fc"
          }

        var visualization = d3plus.viz()
            .container("#ratio_viz")
            .data(data)
            .type("tree_map")
            .id(["gender"])
            .size("value")
            .color(function(d){
              return gender_colours[d.gender];
            })
            .legend({"size": 0})
            .draw()
    }});
});
