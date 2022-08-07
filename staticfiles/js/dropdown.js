let dropdown = $('#coin_name');

dropdown.empty();

dropdown.append('<option selected="true" disabled>Choose a Coin</option>');
dropdown.prop('selectedIndex', 0);

const url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false';


// Populate dropdown with list of cryptocurrencies
$.getJSON(url, function (data) {
  for (items in data) {

    // Gets the id property of each object in the array
    let id = data[items].id
   // Use it in the append
    $("#coin_name").append(
      '<option value="' + id + '">' + id + "</option>",
      console.log(id)
    );}
});

let options = $('#coin_symbol');

options.empty();

options.append('<option selected="true" disabled>Choose a symbol</option>');
options.prop('selectedIndex', 0);


// Populate dropdown with list of cryptocurrencies
$.getJSON(url, function (data) {
  for (items in data) {

    // Gets the id property of each object in the array
    let symbol = data[items].symbol
   // Use it in the append
    $("#coin_symbol").append(
      '<option value="' + symbol +'">' + symbol + "</option>",

    );}
});