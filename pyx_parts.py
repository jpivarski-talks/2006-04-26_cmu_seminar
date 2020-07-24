import pyx
pyx.text.defaulttexrunner = pyx.text.texrunner("latex")
pyx.text.defaulttexrunner.preamble("\AtBeginDocument{\sffamily}")

c = pyx.canvas.canvas()
c.text(0, 0, r"$f_\pi$", [pyx.text.halign.boxcenter])
c.text(0, -0.5, r"$f_K$", [pyx.text.halign.boxcenter])
c.text(0, -1, r"$3M_\Xi - M_N$", [pyx.text.halign.boxcenter])
c.text(0, -1.5, r"$2M_{B_s} - M_\Upsilon$", [pyx.text.halign.boxcenter])
c.text(0, -2, r"$M_{\psi(1P)} - M_{\psi(1S)}$", [pyx.text.halign.boxcenter, pyx.color.rgb.blue])
c.text(0, -2.5, r"$M_{\Upsilon(1D)} - M_{\Upsilon(1S)}$", [pyx.text.halign.boxcenter, pyx.color.rgb.blue])
c.text(0, -3, r"$M_{\Upsilon(2P)} - M_{\Upsilon(1S)}$", [pyx.text.halign.boxcenter])
c.text(0, -3.5, r"$M_{\Upsilon(3S)} - M_{\Upsilon(1S)}$", [pyx.text.halign.boxcenter])
c.text(0, -4, r"$M_{\Upsilon(1P)} - M_{\Upsilon(1S)}$", [pyx.text.halign.boxcenter])
c.writeEPSfile("part_lqcd_success_labels.eps")

c = pyx.canvas.canvas()
c.text(0, 0, r"$\nu$ missing mass$^2$ (GeV$^2$)", [pyx.text.halign.boxcenter])
c.writeEPSfile("part_dmunu_mm_label.eps")

c = pyx.canvas.canvas()
c.text(0, 0, r"Number of Events/0.01 GeV$^2$", [pyx.text.halign.boxcenter])
c.writeEPSfile("part_dmunu_mm_label2.eps")

c = pyx.canvas.canvas()
c.text(0, 0, r"$\displaystyle \Gamma_{ee} = \frac{{M_\Upsilon}^2}{6 \pi^2} \int \sigma(e^+e^- \to \Upsilon) \, dE$", [pyx.text.halign.boxcenter])
c.writeEPSfile("equation.eps")

