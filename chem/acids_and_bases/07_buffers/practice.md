# Practice: Buffers

Assume 25 °C. Use pKa(CH₃COOH) = 4.74 and pKa(NH₄⁺) = 9.26. Try each problem before opening the solution.

---

**1.** Calculate the pH of a buffer that is 0.30 M NH₃ and 0.20 M NH₄Cl.

<details><summary>Show solution</summary>

The acid member is NH₄⁺ and the base member is NH₃.

```
pH = pKa(NH₄⁺) + log([NH₃]/[NH₄⁺]) = 9.26 + log(0.30/0.20) = 9.26 + 0.18 = 9.43
```

</details>

---

**2.** You need 500.0 mL of a buffer at pH 9.00 that is 0.20 M in NH₃. What mass of NH₄Cl (molar mass 53.49 g/mol) must you dissolve?

<details><summary>Show solution</summary>

```
9.00 = 9.26 + log([NH₃]/[NH₄⁺])
[NH₃]/[NH₄⁺] = 10^(−0.26) = 0.56
[NH₄⁺] = 0.20 / 0.56 = 0.36 M
mol NH₄Cl = 0.36 M × 0.5000 L = 0.18 mol
mass = 0.18 mol × 53.49 g/mol = 9.6 g
```

The target pH is below pKa, so you need more NH₄⁺ than NH₃.

</details>

---

**3.** Which weak acid and its sodium salt would make the best buffer at pH 4.0?

(A) HF, pKa 3.17  (B) HCOOH, pKa 3.74  (C) CH₃COOH, pKa 4.74  (D) HOCl, pKa 7.52

<details><summary>Show solution</summary>

**(B).** Its pKa of 3.74 is the closest to 4.0 (0.26 units away), well within the effective range of pKa ± 1. Acetic acid (0.74 away) would work, but less well.

</details>

---

**4.** A buffer contains NH₃ and NH₄Cl. Write the net ionic equation for the reaction that occurs when a small amount of (a) HCl and (b) NaOH is added.

<details><summary>Show solution</summary>

(a) NH₃(aq) + H₃O⁺(aq) → NH₄⁺(aq) + H₂O(l)

(b) NH₄⁺(aq) + OH⁻(aq) → NH₃(aq) + H₂O(l)

In each case, the strong acid or base is replaced by the weak member of the pair, so the pH changes only slightly.

</details>

---

**5.** Two buffers are made from the weak acid HA (pKa = 5.00) and its conjugate base A⁻:

- Buffer X: 0.50 M HA and 0.10 M A⁻
- Buffer Y: 0.10 M HA and 0.50 M A⁻

(a) Which buffer has the higher pH?
(b) Which buffer can neutralize more added NaOH before its pH changes significantly? Justify your answer.

<details><summary>Show solution</summary>

(a) **Buffer Y.** It has more base than acid: pH = 5.00 + log(5) = 5.70. Buffer X is 5.00 + log(0.2) = 4.30.

(b) **Buffer X.** Added OH⁻ is neutralized by the **acid** member (HA + OH⁻ → A⁻ + H₂O). X contains five times more HA than Y, so it can absorb more OH⁻ before the HA runs out.

</details>

---

**6.** A buffer solution is diluted with water to 10 times its original volume. Which statement is correct?

(A) The pH increases by 1 unit and the buffer capacity decreases.
(B) The pH stays about the same and the buffer capacity decreases.
(C) The pH stays about the same and the buffer capacity stays the same.
(D) The pH decreases by 1 unit and the buffer capacity increases.

<details><summary>Show solution</summary>

**(B).** Both [HA] and [A⁻] drop by the same factor, so the ratio [A⁻]/[HA], and therefore the pH, stays the same. There are fewer particles per liter to neutralize added acid or base, so the capacity decreases.

</details>

---

**7.** How many milliliters of 0.500 M NaOH must be added to 100.0 mL of 0.200 M CH₃COOH to make a buffer with pH 5.00?

<details><summary>Show solution</summary>

```
Target ratio: [CH₃COO⁻]/[CH₃COOH] = 10^(5.00 − 4.74) = 1.8
mmol CH₃COOH initially = 100.0 × 0.200 = 20.0 mmol
```

Let n = mmol OH⁻ added. After the reaction there are n mmol of CH₃COO⁻ and (20.0 − n) mmol of CH₃COOH.

```
n / (20.0 − n) = 1.8
n = 1.8 × 20.0 / 2.8 = 12.9 mmol
V = 12.9 mmol / 0.500 M = 25.7 mL
```

</details>

---

**8.** A diagram of a buffer solution shows 6 HA particles and 6 A⁻ particles (water molecules not shown). Then 2 OH⁻ ions are added.

(a) How many HA and A⁻ particles are present after the reaction?
(b) Is the new pH greater than, less than, or equal to the pKa of HA? Justify your answer.

<details><summary>Show solution</summary>

(a) Each OH⁻ converts one HA into one A⁻ (HA + OH⁻ → A⁻ + H₂O), leaving **4 HA and 8 A⁻**.

(b) **Greater than pKa.** Now [A⁻] > [HA], so log([A⁻]/[HA]) = log(2) > 0, and pH = pKa + 0.30.

</details>

---

**9. Beyond the AP exam (your class tests may still ask this).** 0.010 mol of HCl is added to 1.00 L of the buffer from Example 1 in the notes (0.25 M CH₃COOH, 0.40 M CH₃COO⁻, pH 4.95). Assume no volume change.

(a) Calculate the new pH.
(b) Compare with adding the same HCl to 1.00 L of pure water.

<details><summary>Show solution</summary>

(a) The H₃O⁺ reacts with acetate:
```
             CH₃COO⁻  +  H₃O⁺  →  CH₃COOH  +  H₂O
Before (mol)  0.40       0.010     0.25
After         0.39       0         0.26
pH = 4.74 + log(0.39/0.26) = 4.74 + 0.18 = 4.92
```

The pH dropped by only about **0.03 units**.

(b) In pure water, [H₃O⁺] = 0.010 M, so the pH would fall from 7.00 to **2.00**, a drop of 5 units. The buffer reduced the change by a factor of more than 100.

</details>

➡️ Next topic: [8. pH and solubility](../08_ph_and_solubility/notes.md)
