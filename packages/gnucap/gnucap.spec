Name:           gnucap
Version:        0.35
Release:        29%{?dist}
Summary:        The Gnu Circuit Analysis Package
License:        GPLv2+
URL:            http://www.gnu.org/software/gnucap/
Source0:        http://www.gnucap.org/devel/gnucap-%{version}.tar.gz
Patch0:         gnucap-0.34-debian.patch
Patch1:         gnucap-0.35-gcc43.patch
Patch2:         gnucap-0.35-gcc6.patch
BuildRequires:  gcc-c++
BuildRequires:  readline-devel

%description
The primary component is a general purpose circuit simulator. It performs
nonlinear dc and transient analyses, fourier analysis, and ac analysis. Spice
compatible models for the MOSFET (level 1-7), BJT, and diode are included in
this release. Gnucap is not based on Spice, but some of the models have been
derived from the Berkeley models. Unlike Spice, the engine is designed to do
true mixed-mode simulation. Most of the code is in place for future support of
event driven analog simulation, and true multi-rate simulation.


%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
# use ncurses instead of termcap (bz 226771)
sed -i 's/-ltermcap/-lncurses/g' configure


%build
%configure
make %{?_smp_mflags}


%install
%make_install

# for %%doc
rm -r $RPM_BUILD_ROOT%{_datadir}/%{name}
mv doc/acs-tutorial doc/gnucap-tutorial
rm examples/Makefile*


%files
%doc doc/history doc/relnotes.* doc/gnucap-tutorial doc/whatisit
%doc man/gnucap-man.pdf examples
%license doc/COPYING
%{_bindir}/%{name}*
%{_mandir}/man1/%{name}.1.gz


%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.35-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.35-28
- Rebuild for readline 8.0

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.35-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.35-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 07 2018 Adam Williamson <awilliam@redhat.com> - 0.35-25
- Rebuild to fix GCC 8 mis-compilation
  See https://da.gd/YJVwk ("GCC 8 ABI change on x86_64")

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.35-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.35-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.35-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.35-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.35-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.35-19
- Rebuild for readline 7.x

* Tue Apr 26 2016 Hans de Goede <hdegoede@redhat.com> - 0.35-18
- Fix building with gcc 6 (rhbz#1307551)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.35-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.35-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.35-15
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.35-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.35-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.35-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.35-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.35-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.35-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.35-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jan 13 2010 Rakesh Pandit <rakesh@fedoraproject.org> - 0.35-7
- Fixed URL and Source0

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.35-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.35-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.35-4
- Autorebuild for GCC 4.3

* Tue Jan  8 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.35-3
- Fix building with gcc 4.3

* Tue Aug  7 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.35-2
- Update License tag for new Licensing Guidelines compliance

* Wed Feb 14 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.35-1
- New upstream release 0.35
- Link with -lncurses instead of -ltermcap (bz 226771)

* Mon Aug 28 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 0.34-3
- FE6 Rebuild

* Thu Apr 27 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 0.34-2
- add %%{?_smp_mflags} to the make command (bz 189699)

* Sun Apr 23 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 0.34-1
- Initial spec file
