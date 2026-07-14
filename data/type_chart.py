# Contains the weaknesses of every Pokemon type present in
# the Generation 1 and Generation 2 datasets.

type_chart = {

    "Normal": {
        "weak_against": ["Fighting"]
    },

    "Fire": {
        "weak_against": ["Water", "Ground", "Rock"]
    },

    "Water": {
        "weak_against": ["Electric", "Grass"]
    },

    "Electric": {
        "weak_against": ["Ground"]
    },

    "Grass": {
        "weak_against": ["Fire", "Ice", "Poison", "Flying", "Bug"]
    },

    "Ice": {
        "weak_against": ["Fire", "Fighting", "Rock", "Steel"]
    },

    "Fighting": {
        "weak_against": ["Flying", "Psychic"]
    },

    "Poison": {
        "weak_against": ["Ground", "Psychic"]
    },

    "Ground": {
        "weak_against": ["Water", "Grass", "Ice"]
    },

    "Flying": {
        "weak_against": ["Electric", "Ice", "Rock"]
    },

    "Psychic": {
        "weak_against": ["Bug", "Ghost", "Dark"]
    },

    "Bug": {
        "weak_against": ["Fire", "Flying", "Rock"]
    },

    "Rock": {
        "weak_against": ["Water", "Grass", "Fighting", "Ground", "Steel"]
    },

    "Ghost": {
        "weak_against": ["Ghost", "Dark"]
    },

    "Dragon": {
        "weak_against": ["Ice", "Dragon"]
    },

    "Dark": {
        "weak_against": ["Fighting", "Bug"]
    },

    "Steel": {
        "weak_against": ["Fire", "Fighting", "Ground"]
    },

    "Fairy": {
        "weak_against": ["Poison", "Steel"]
    }

}