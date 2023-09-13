<script>
  let team
  let points
  let letter
  let returned
  let napis = ""
  let dane = ""
  function addPoints() {
    fetch(`http://130.61.172.11:8000/addpoints/${team}/${points}`)
  }
  function odkryjLitere(litera) {
    fetch(`http://130.61.172.11:8000/uncover/${litera}`)
  }
  function odkryj() {
    fetch("http://130.61.172.11:8000/uncover")
  }
  function ustawNapis() {
    fetch(`http://130.61.172.11:8000/setphrase/${napis}`)
  }
  function spin() {
    fetch("http://130.61.172.11:8000/spin")
  }
  setInterval(()=> {
    refresh();
  }, 200)
  function refresh() {
    fetch("http://130.61.172.11:8000/").then(x => x.text()).then(data => dane = data).then(() => returned = JSON.parse(dane) )
  }
</script>

<main>
  <div>
    <h1>Strefa Dodawania Punktów</h1>
      <label for="fname">NUMER DRUŻYNY:</label><br>
      <input type="number" bind:value={team}><br>
      <label for="lname">ILOŚĆ PUNKTÓW:</label><br>
      <input type="number" bind:value={points}><br><br>
      <input type="button" value="Submit" on:click={addPoints}>
  </div>
  <div>
    <h1>Strefa Ustawiania Napisu i Odkrywania Liter</h1>
      <label for="fname">Ustaw Napis (sam się zacenzuruje):
      </label><input type="text" bind:value={napis}>
      <input type="button" value="Submit" on:click={ustawNapis}><br>
      <label for="lname">Odkryj literę o numerze:</label>
      <input type="number" bind:value={letter}>
      <input type="button" value="Submit" on:click={() => odkryjLitere(letter-1)}>
      <button on:click={odkryj}>Odkryj Wszystko</button>
  </div>
  <div>
    <h1>Strefa Interaktywnego Odkrywania Liter</h1>
    {#if returned != undefined}
      {#each returned.uncovered as letter, i}
        <button class="odkrywajka" on:click={() => odkryjLitere(i)}>{letter}</button>
      {/each}
    {/if}
  </div>
  <div>
    <h1>Strefa KRĘCENIA</h1>
      <input type="button" value="SPIN" class="SPIN" on:click={spin}>
  </div>
  <div>

      {#await dane}
        <p>Loading data...</p>
      {:then result}
        {@html result}
      {/await}
  </div>
</main>

<style>
  .odkrywajka {
    width: 3rem;
    height: 3rem;
    
  }
  main {
    position: absolute;
    top: 0;
    bottom: 0;
    right: 0;
    left: 0;
    padding: 2rem;
    background-color: #222;
    color: rgb(209, 127, 127);
  }
  input {
    background-color: #222;
    color: rgb(209, 127, 127);
    border: 1px solid rgb(209, 127, 127);
    cursor: pointer;
    border-radius: 5px;
  }
  button {
    background-color: #222;
    color: rgb(209, 127, 127);
    border: 1px solid rgb(209, 127, 127);
    cursor: pointer;
    border-radius: 5px;
  }
  .SPIN{
    font-size: 5rem;
    padding: 5rem;
  }
</style>
