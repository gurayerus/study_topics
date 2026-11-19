# Practice: Weak acids and bases

Assume 25 °C, where Kw = 1.0 × 10⁻¹⁴. Try each problem before opening the solution.

---

**1.** Calculate the pH and percent ionization of 0.25 M HNO₂ (Ka = 4.5 × 10⁻⁴).

<details><summary>Show solution</summary>

```
HNO₂ + H₂O ⇌ H₃O⁺ + NO₂⁻
Ka = x² / (0.25 − x) ≈ x² / 0.25 = 4.5 × 10⁻⁴
x  = √(1.125 × 10⁻⁴) = 0.011 M = [H₃O⁺]
pH = −log(0.0106) = 1.97
% ionization = 0.0106 / 0.25 × 100 = 4.2%
```

4.2% is under 5%, so the approximation holds. Solving the quadratic gives pH 1.98, which is essentially the same.

</details>

---

**2.** A 0.150 M solution of a weak monoprotic acid HA has a pH of 2.85. Calculate Ka and the percent ionization.

<details><summary>Show solution</summary>

```
[H₃O⁺] = 10^(−2.85) = 1.41 × 10⁻³ M = [A⁻]
[HA]   = 0.150 − 0.00141 = 0.149 M
Ka     = (1.41 × 10⁻³)² / 0.149 = 1.3 × 10⁻⁵
% ionization = 1.41 × 10⁻³ / 0.150 × 100 = 0.94%
```

</details>

---

**3.** Consider 0.10 M solutions of HF (Ka = 6.8 × 10⁻⁴), HOCl (Ka = 3.0 × 10⁻⁸), and HCN (Ka = 6.2 × 10⁻¹⁰).

(a) Rank the three solutions from lowest to highest pH.

(b) Rank the conjugate bases F⁻, OCl⁻, and CN⁻ from weakest to strongest base. Justify your answer.

<details><summary>Show solution</summary>

(a) **HF < HOCl < HCN.** At equal concentrations, a larger Ka means more ionization, so more H₃O⁺ and a lower pH. The actual values are about 2.10, 4.26, and 5.10.

(b) **F⁻ < OCl⁻ < CN⁻.** Since Ka × Kb = Kw, the weakest acid has the strongest conjugate base. HCN has the smallest Ka, so CN⁻ has the largest Kb (1.6 × 10⁻⁵).

</details>

---

**4.** Calculate the pH of 0.050 M methylamine, CH₃NH₂ (Kb = 4.4 × 10⁻⁴). Check whether the small-x approximation is valid.

<details><summary>Show solution</summary>

```
CH₃NH₂ + H₂O ⇌ CH₃NH₃⁺ + OH⁻
Approximation:  x = √(4.4 × 10⁻⁴ × 0.050) = 4.7 × 10⁻³ M
5% check:       4.7 × 10⁻³ / 0.050 = 9.4%   →  more than 5%, so the approximation fails
```

Solve the quadratic instead:

```
x² / (0.050 − x) = 4.4 × 10⁻⁴
x² + (4.4 × 10⁻⁴)x − 2.2 × 10⁻⁵ = 0
x = [−4.4 × 10⁻⁴ + √((4.4 × 10⁻⁴)² + 4(2.2 × 10⁻⁵))] / 2 = 4.5 × 10⁻³ M = [OH⁻]
pOH = 2.35        pH = 11.65
```

The approximation would have given pH 11.67. Even when it fails, the error is small, but the check is what tells you whether to trust it.

</details>

---

**5.** Calculate the pH of 0.10 M NaOCl (Ka of HOCl = 3.0 × 10⁻⁸).

<details><summary>Show solution</summary>

Na⁺ has no effect, and OCl⁻ is the conjugate base of a weak acid.

```
OCl⁻ + H₂O ⇌ HOCl + OH⁻
Kb    = 1.0 × 10⁻¹⁴ / 3.0 × 10⁻⁸ = 3.3 × 10⁻⁷
[OH⁻] = √(3.3 × 10⁻⁷ × 0.10) = 1.8 × 10⁻⁴ M
pOH = 3.74        pH = 10.26
```

Household bleach is basic partly for this reason.

</details>

---

**6.** Classify each 0.10 M solution as acidic, basic, or neutral.

(a) NaCl (b) NH₄Cl (c) KNO₂ (d) NaClO₄ (e) CH₃NH₃Br (f) Na₂CO₃

<details><summary>Show solution</summary>

| Salt | Cation | Anion | Result |
|---|---|---|---|
| (a) NaCl | Na⁺ (no effect) | Cl⁻ (no effect) | **neutral** |
| (b) NH₄Cl | NH₄⁺ (weak acid) | Cl⁻ (no effect) | **acidic** |
| (c) KNO₂ | K⁺ (no effect) | NO₂⁻ (weak base) | **basic** |
| (d) NaClO₄ | Na⁺ (no effect) | ClO₄⁻ (no effect) | **neutral** |
| (e) CH₃NH₃Br | CH₃NH₃⁺ (weak acid) | Br⁻ (no effect) | **acidic** |
| (f) Na₂CO₃ | Na⁺ (no effect) | CO₃²⁻ (weak base) | **basic** |

</details>

---

**7.** Rank the following species in 0.10 M HF from highest to lowest concentration: HF, H₃O⁺, F⁻, OH⁻.

<details><summary>Show solution</summary>

**HF > H₃O⁺ ≈ F⁻ > OH⁻.** HF is weak, so most of it stays un-ionized. Each HF that ionizes makes one H₃O⁺ and one F⁻, so those two are about equal. The solution is acidic, so [OH⁻] is tiny (Kw / [H₃O⁺]).

</details>

---

**8.** A solution of a weak acid with a very small Ka is diluted from 0.10 M to 0.0010 M. How does its percent ionization change?

(A) It decreases by a factor of about 10.
(B) It stays the same.
(C) It increases by a factor of about 10.
(D) It increases by a factor of about 100.

<details><summary>Show solution</summary>

**(C).** With the small-x approximation, % ionization = √(Ka × C) / C × 100 = √(Ka / C) × 100. Making C 100 times smaller makes the percent ionization √100 = 10 times larger. For HOCl, it goes from 0.055% to 0.55%. Conceptually, dilution makes Q < Ka, so the equilibrium shifts toward the ions.

</details>

---

**9. (Free-response style)** A student measures the pH of a 0.20 M solution of a weak base B to be 10.50.

(a) Write the equation for the reaction of B with water.

(b) Calculate Kb for B.

(c) Calculate Ka for the conjugate acid HB⁺.

(d) The student dilutes the solution to 0.020 M. Will the pH increase, decrease, or stay the same? Will the percent ionization increase, decrease, or stay the same? Justify both answers.

<details><summary>Show solution</summary>

(a) B(aq) + H₂O(l) ⇌ HB⁺(aq) + OH⁻(aq)

(b)
```
pOH   = 14.00 − 10.50 = 3.50
[OH⁻] = 10^(−3.50) = 3.2 × 10⁻⁴ M = [HB⁺]
Kb    = (3.2 × 10⁻⁴)² / (0.20 − 0.00032) = 5.0 × 10⁻⁷
```

(c) Ka = Kw / Kb = 1.0 × 10⁻¹⁴ / 5.0 × 10⁻⁷ = 2.0 × 10⁻⁸

(d) **The pH decreases** (the solution becomes less basic) because [OH⁻] ≈ √(Kb × C) is smaller when C is smaller. **The percent ionization increases.** Dilution lowers Q below Kb (two ion concentrations on top, one on the bottom), so the equilibrium shifts right and a larger fraction of B reacts.

</details>

➡️ Next topic: [3. Acid–base reactions and mixtures](../03_acid_base_reactions/notes.md)
