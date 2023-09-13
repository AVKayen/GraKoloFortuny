<script>
  let pix = 0;
  let value = "";
  let dane;
  let pytanie = "";
  let tablica = [];
  let literki = "";
  let spinning = false;
  function refresh() {
    fetch("http://130.61.172.11:8000/")
      .then((x) => x.json())
      .then((data) => (dane = data))
      .then(() =>{
        tablica = dane.points;
        literki = dane.phrase;
        if (dane.isSpin && !spinning) {
          spin();
        }
      })
  }
  setInterval(() => {
    refresh();
  }, 300);
  function spin() {
    spinning = true;
    let randomValue = Math.random();
    let spin = 30 + 42 * randomValue;
    const interval = setInterval(function () {
      pix += spin;
      spin -= spin / 36;
      if (spin <= 0.01) {
        clearInterval(interval);
        spinning = false;
        let v = pix % 360;
        console.log(v, v/18, 20 - Math.ceil(v/18))
        let expectedValue = (20 - ((Math.ceil(v / 18))));
        value = slices.find(x => x.search_id == expectedValue).label;
        console.log(expectedValue)
        if (value == "SKIP") {
          pytanie = "SKIP!!!"
        } else {
          pytanie = dane.question;
        }
      }
    }, 10);
  }
  let slices = [
    { id: 1, search_id: 16, color: "000", label: "BANKRUT", label_color: "white" },
    { id: 2, search_id: 17, color: "f3722c", label: "300" },
    { id: 3, search_id: 18, color: "f9844a", label: "400" },
    { id: 4, search_id: 19, color: "f8961e", label: "500" },
    { id: 5, search_id: 0, color: "fff", label: "SKIP" },
    { id: 6, search_id: 1, color: "90be6d", label: "600" },
    { id: 7, search_id: 2, color: "43aa8b", label: "300" },
    { id: 8, search_id: 3, color: "4d908e", label: "400" },
    { id: 9, search_id: 4, color: "577590", label: "500" },
    { id: 10, search_id: 5, color: "277da1", label: "400" },
    { id: 11, search_id: 6, color: "f3722c", label: "300" },
    { id: 12, search_id: 7, color: "f9844a", label: "500" },
    { id: 13, search_id: 8, color: "fff", label: "SKIP" },
    { id: 14, search_id: 9, color: "f8961e", label: "200" },
    { id: 15, search_id: 10, color: "f9c74f", label: "300" },
    { id: 16, search_id: 11, color: "90be6d", label: "500" },
    { id: 17, search_id: 12, color: "43aa8b", label: "200" },
    { id: 18, search_id: 13, color: "4d908e", label: "500" },
    { id: 19, search_id: 14, color: "577590", label: "300" },
    { id: 20, search_id: 15, color: "277da1", label: "500" },
  ];
</script>

<main>
  <div class="kolo" style="transform: rotate({pix}deg);">
    {#each slices as slice}
      <div
        class="slice"
        style="background-color: #{slice.color}; color: {slice.label_color}; transform: rotate({18 *
          slice.id}deg"
      >
        <p class="label">{slice.label}</p>
      </div>
    {/each}
  </div>
  <h1 class="value">{value}</h1>
  <div class="ziutek" />
</main>
<div class="mainer">
  <div class="pytanie"><p class="pytaj">PYTANIE: </p><br /> {pytanie}?</div>
  <div class="linia">

  </div>
  <div class="litery">
    {#each literki as litera}
      {#if litera == ' '}
      <div class="litery">
      </div>
      {:else if litera == '*'}
      <div class="litera zakryte"></div>
      {:else}
      <div class="litera">{litera}</div>
      {/if}
    {/each}
  </div>
</div>
<div class="punkty">
  <div class="punkt">1B: <b>{tablica[0]}</b></div>
  <div class="punkt">2B: <b>{tablica[1]}</b></div>
  <div class="punkt">3B: <b>{tablica[2]}</b></div>
  <div class="punkt">4B: <b>{tablica[3]}</b></div>
</div>
<style>
  .linia {
    height: 2px;
    background-color: white;
    width: 100%;
    margin-bottom: 4rem;
    margin-top: 1rem;
  }
  .value {
    position: absolute;
    font-size: 5rem;
    left: 50%;
    top: -3rem;
    transform: translate(-50%);
    text-transform: uppercase;
    color: white;
    font-family: sans-serif;
    border-radius: 100%;
    padding: 30px;
    aspect-ratio: 1 / 1;
    text-align: center;
    justify-content: center;
  }
  .litery {
    width: 100%;
    display: flex;
    flex-wrap: wrap;
    flex-direction: row;
    align-items: center;
    justify-content: center;
  }
  .litera {
    border: #fff solid 1px;
    border-radius: 2px;
    padding: 20px;
    color: white;
    width: 3rem;
    height: 3rem;
    margin: 3px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #fff;
    font-size: 3rem;
  }
  .zakryte {
    background-color: #fff;
  }
  .mainer {
    position: absolute;
    top: 0;
    right: 0;
    margin: 10rem;
    width: 50%;
  }
  .punkty {
    width: 100vw;
    display: flex;
    left: 0;
    flex-direction: row;
    justify-content: space-evenly;
    position: absolute;
    bottom: 2rem;
    color: white;
    font-family: sans-serif;
    font-size: 5rem;
    
  }
  .punkt {
    margin: 1rem;
    padding: 1rem;
    align-items: center;
    justify-items: center;
    background-color: #121212;
    border-radius: 1rem;
    width: 20vw;
  }
  .pytanie {
    width: 100%;
    text-align: center;
    color: white;
    font-family: sans-serif;
    font-size: 2.5rem;
  }
  .pytaj {
    font-size: 2rem !important;
  }
  .ziutek {
    position: absolute;
    left: 50%;
    width: 4px;
    height: 30px;
    top: 9rem;
    transform: translate(-2px);
    background-color: aqua;
  }
  .kolo {
    position: relative;
    width: 50vmin;
    height: 50vmin;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  main {
    position: absolute;
    top: 0;
    left: 0;
    padding: 10rem;
  }
  .slice {
    display: block;
    position: absolute;
    width: 100%;
    height: 100%;
    border-radius: 50%;
    clip-path: polygon(0% 50%, 0% 33.6%, 51% 50%, 0% 50%);
    overflow: hidden;
  }

  .label {
    position: relative;
    top: 44%;
    left: 6%;
    transform: rotate(9deg);
    font-size: 2rem;
  }
</style>
