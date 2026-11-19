# 2. Weak acids and bases

AP topic **8.3 Weak Acid and Base Equilibria**

> **Goal:** Find the pH, percent ionization, and concentrations of every species in a solution of a weak acid or weak base. Go the other way too: find Ka from a measured pH.

## What makes an acid weak

A weak acid ionizes only a little. Most of it stays as intact HA molecules, so the reaction is an equilibrium:

```
HA(aq) + H₂O(l) ⇌ H₃O⁺(aq) + A⁻(aq)          Ka = [H₃O⁺][A⁻] / [HA]
```

In 0.10 M acetic acid, only about 1 molecule in 75 is ionized. Ranking the species in the beaker by concentration:

```
[HA]  ≫  [H₃O⁺] ≈ [A⁻]  ≫  [OH⁻]
```

AP questions often show particle diagrams. A weak acid is drawn as mostly intact HA with just a few H₃O⁺ / A⁻ pairs. A strong acid is drawn with no HA at all.

| | pKa = −log Ka |
|---|---|
| **Smaller Ka (larger pKa)** | weaker acid, less ionized, higher pH at the same concentration |
| **Larger Ka (smaller pKa)** | stronger acid |

### Ka values used in this folder

| Acid | Ka | pKa |
|---|---|---|
| HF | 6.8 × 10⁻⁴ | 3.17 |
| HNO₂ | 4.5 × 10⁻⁴ | 3.35 |
| HCOOH (formic) | 1.8 × 10⁻⁴ | 3.74 |
| CH₃COOH (acetic) | 1.8 × 10⁻⁵ | 4.74 |
| HOCl | 3.0 × 10⁻⁸ | 7.52 |
| HCN | 6.2 × 10⁻¹⁰ | 9.21 |

| Base | Kb | pKb |
|---|---|---|
| NH₃ | 1.8 × 10⁻⁵ | 4.74 |
| CH₃NH₂ (methylamine) | 4.4 × 10⁻⁴ | 3.36 |

On the exam, Ka and Kb values are always given. You don't need to memorize them.

## Weak bases work the same way

A weak base takes a proton from water, making OH⁻:

```
B(aq) + H₂O(l) ⇌ HB⁺(aq) + OH⁻(aq)          Kb = [HB⁺][OH⁻] / [B]
```

Typical weak bases are NH₃, amines (CH₃NH₂ and similar), and the conjugate bases of weak acids (F⁻, CH₃COO⁻, OCl⁻, CN⁻).

## The ICE-table method

**Example 1. Find the pH of 0.10 M CH₃COOH (Ka = 1.8 × 10⁻⁵).**

```
            CH₃COOH  +  H₂O  ⇌  H₃O⁺  +  CH₃COO⁻
Initial      0.10                  0         0
Change       −x                   +x        +x
Equil.       0.10 − x              x         x
```

```
Ka = x² / (0.10 − x) = 1.8 × 10⁻⁵
```

**Small-x approximation.** Ka is small, so x will be tiny compared with 0.10. Treat 0.10 − x as 0.10:

```
x² / 0.10 = 1.8 × 10⁻⁵    →    x = √(1.8 × 10⁻⁶) = 1.3 × 10⁻³ M = [H₃O⁺]
pH = −log(1.3 × 10⁻³) = 2.87
```

**Check the 5% rule:** (x / initial) × 100 = (1.3 × 10⁻³ / 0.10) × 100 = 1.3%. That's under 5%, so the approximation is fine.

For a weak acid, the shortcut is:

```
[H₃O⁺] ≈ √(Ka × C)        [OH⁻] ≈ √(Kb × C)  for a weak base
```

### When the 5% check fails

If x / C comes out above 5%, solve the quadratic instead. In Example 1, that would mean rearranging x² = Ka(0.10 − x) into x² + Ka·x − Ka·C = 0 and using the quadratic formula. The [practice set](practice.md) has one of these (problem 4). AP problems are usually designed so that the approximation works, but the check shows you understand when it applies.

## Percent ionization

```
% ionization = [H₃O⁺]eq / [HA]initial × 100
```

Diluting a weak acid **increases** its percent ionization, even though [H₃O⁺] goes down.

| CH₃COOH concentration | [H₃O⁺] | pH | % ionized |
|---|---|---|---|
| 0.10 M | 1.3 × 10⁻³ M | 2.87 | 1.3% |
| 0.010 M | 4.2 × 10⁻⁴ M | 3.37 | 4.2% |

**Why:** Dilution lowers every concentration. Q = [H₃O⁺][A⁻]/[HA] has two concentrations on top and one on the bottom, so Q drops below Ka and the reaction shifts right, ionizing a larger fraction.

## Going backward: Ka from pH

**Example 2. A 0.050 M solution of a weak acid HA has a pH of 3.00. Calculate Ka.**

```
[H₃O⁺] = 10^(−3.00) = 1.0 × 10⁻³ M = [A⁻]
[HA]   = 0.050 − 0.0010 = 0.049 M
Ka     = (1.0 × 10⁻³)² / 0.049 = 2.0 × 10⁻⁵
```

## Conjugate pairs: Ka × Kb = Kw

For any conjugate acid–base pair:

```
Ka × Kb = Kw = 1.0 × 10⁻¹⁴        pKa + pKb = 14.00   (25 °C)
```

So the **weaker the acid, the stronger its conjugate base**:

| Acid | Ka | Conjugate base | Kb |
|---|---|---|---|
| HF | 6.8 × 10⁻⁴ | F⁻ | 1.5 × 10⁻¹¹ |
| HOCl | 3.0 × 10⁻⁸ | OCl⁻ | 3.3 × 10⁻⁷ |
| HCN | 6.2 × 10⁻¹⁰ | CN⁻ | 1.6 × 10⁻⁵ |

The conjugate base of a *strong* acid (Cl⁻, Br⁻, I⁻, NO₃⁻, ClO₄⁻) is so weak that it has no measurable effect on pH.

## Salt solutions: acidic, basic, or neutral?

A salt is made of a cation and an anion. Look at each ion separately:

| Ion | Effect on pH | Examples |
|---|---|---|
| Cation of a strong base | none | Na⁺, K⁺, Ca²⁺, Ba²⁺ |
| Anion of a strong acid | none | Cl⁻, Br⁻, NO₃⁻, ClO₄⁻ |
| Conjugate acid of a weak base | acidic | NH₄⁺, CH₃NH₃⁺ |
| Conjugate base of a weak acid | basic | F⁻, CH₃COO⁻, OCl⁻, CN⁻, NO₂⁻ |

**Example 3. Find the pH of 0.10 M NaF (Ka of HF = 6.8 × 10⁻⁴).**

Na⁺ has no effect. F⁻ is a weak base:

```
F⁻(aq) + H₂O(l) ⇌ HF(aq) + OH⁻(aq)
Kb = Kw / Ka = 1.0 × 10⁻¹⁴ / 6.8 × 10⁻⁴ = 1.5 × 10⁻¹¹
[OH⁻] = √(1.5 × 10⁻¹¹ × 0.10) = 1.2 × 10⁻⁶ M
pOH = 5.92        pH = 14.00 − 5.92 = 8.08
```

The solution is slightly basic, as expected. The same reasoning gives the pH at the equivalence point of a titration (folders 3 and 4).

**Example 4. Find the pH of 0.20 M NH₃ (Kb = 1.8 × 10⁻⁵).**

```
[OH⁻] = √(1.8 × 10⁻⁵ × 0.20) = 1.9 × 10⁻³ M      (0.95%, passes the 5% check)
pOH = 2.72        pH = 11.28
```

## Common mistakes

- **Treating a weak acid as strong.** If a Ka is given, set up an equilibrium. The pH of 0.10 M acetic acid is 2.87, not 1.00.
- **Using Ka for a base problem.** For F⁻, CH₃COO⁻, NH₃, and similar, you need Kb. Convert with Kb = Kw / Ka, then get pOH before pH.
- **Skipping the 5% check.** It takes five seconds and protects you when x isn't small.
- **Thinking dilution lowers percent ionization.** It's the opposite.
- **Forgetting that x is the [H₃O⁺] from the acid only.** Water's contribution is negligible unless the solution is extremely dilute or the acid extremely weak.

➡️ Next: [practice.md](practice.md)
