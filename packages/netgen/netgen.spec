Name:             netgen
Version:          1.3.7
Release:          37%{?dist}
Summary:          LVS netlist comparison tool for VLSI

License:          GPL+
URL:              http://opencircuitdesign.com/netgen

Source0:          http://opencircuitdesign.com/%{name}/archive/%{name}-%{version}.tgz
Source1:          %{name}.desktop
# this png is a screenshot taken on adder4 (an alliance's example) by Chitlesh
# its license is GPL+
Source2:          %{name}.png

Patch0:           netgen-1.3.7-free.patch

BuildRequires:  gcc
BuildRequires:    tk-devel m4 libXt-devel desktop-file-utils
Requires:         coreutils gtk2

%description
Netgen is a tool for comparing netlists, a process known as LVS,
which stands for "Layout vs. Schematic". This is an important step
in the integrated circuit design flow, ensuring that the geometry
that has been laid out matches the expected circuit.

The greatest need for LVS is in large analog or mixed-signal circuits
that cannot be simulated in reasonable time. Even for small circuits,
LVS can be done much faster than simulation, and provides feedback
that makes it easier to find an error than does a simulation.

%prep
# tarball includes unneeded symlink, so we firstly
# create a directory and expand tarball there.
%setup -q -T -c %{name}-%{version} -a 0

%patch0 -p0 -b .free

cd %{name}-%{version}

#fix for 64 bit hardcoded scripts
%ifarch x86_64 ppc64
%{__sed} -i 's|libdir = @libdir@|libdir = /usr/lib64|' scripts/defs.mak.in
%endif

%{__sed} -i.libexec "s|\${LIBDIR}|%{_libexecdir}|" lib/Makefile

%{__sed} -i.cflags -e 's|CFLAGS=.*CFLAGS|:|' configure

%{__sed} -i 's|magic-hackers@csl.cornell.edu|http://bugzilla.redhat.com|' scripts/configure

%{__sed} -i 's|package require -exact|package require|' tcltk/tkcon.tcl

export WISH=/usr/bin/wish

%build
cd %{name}-%{version}

%configure --with-tcl=%{_libdir}      --with-tk=%{_libdir} \
           --with-tcllibs=%{_libdir}  --with-tklibs=%{_libdir}

%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%{__mkdir} -p %{buildroot}%{_libexecdir}/%{name}

cd %{name}-%{version}
%{__make} install                \
    DESTDIR=%{buildroot}         \
    INSTALL="%{__install} -c -p" \
    CP="%{__cp} -p"

chmod 755 %{buildroot}%{_libexecdir}/%{name}/ntk2adl.sh
chmod 755 %{buildroot}%{_libexecdir}/%{name}/spice

# applying timestamps
%{__cp} -p README VERSION TO_DO Changes Copying doc/netgen.doc ..

#removing duplicates
%{__rm} -rf %{buildroot}%{_libdir}/%{name}/doc


# Ensure (on x86_64) that netgen isn't linked to tk.i386 if the latter is installed
sed -i '/NETGEN_WISH/aexport\ TCLIBPATH=%{_libdir}' %{buildroot}%{_bindir}/%{name}

desktop-file-install \
  --dir %{buildroot}%{_datadir}/applications \
  --add-category "Electronics"               \
  %{SOURCE1}

install -d %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/
install -p -m 644 %{SOURCE2} %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}.png

%files
%doc README VERSION TO_DO Changes Copying netgen.doc
%{_bindir}/*
%{_libdir}/%{name}/
%{_libexecdir}/%{name}/
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png


%Changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.3.7-33
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.7-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.7-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Apr 29 2013 Jon Ciesla <limburgher@gmail.com> - 1.3.7-24
- Drop desktop vendor tag.

* Mon Sep 15 2008 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 1.3.7-16
- rebuild for rawhide

* Sun Apr 6 2008 Thibault North <tnorth [AT] fedoraproject DOT org> -1.3.7-15
- fixed compilation for current Tk version

* Sun Jan 13 2008 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 1.3.7-14
- rebuilt for TCL 8.5 #428540

* Sun Oct 21 2007 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 1.3.7-13
- added coreutils and gtk as requires: #339771

* Thu Aug 23 2007 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 1.3.7-12
- complying to freedesktop policies - categories

* Wed Aug 22 2007 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 1.3.7-11
- added desktop file and icon

* Fri Aug 17 2007 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 1.3.7-10
- fix for 64 bit and moved scripts to %%{_libexecdir}/%%{name}/

* Thu Aug 16 2007 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 1.3.7-9
- Ensure (on x86_64) that netgen isn't linked to tk.i386 if the latter is installed

* Tue Aug 14 2007 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 1.3.7-8
- added patch netgen-1.3.7-free.patch by Denis Leroy

* Mon Apr 30 2007 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 1.3.7-7
- removing netgen.doc duplicate

* Mon Apr 23 2007 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 1.3.7-6
- fixed %%configure for 64 arch

* Wed Apr 11 2007 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 1.3.7-5
- Third fix for 64 bit arch

* Thu Mar 22 2007 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 1.3.7-4
- fix for 64 bit

* Sat Mar 17 2007 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 1.3.7-3
- fix for 64 bit hardcoded scripts

* Wed Jan 31 2006 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 1.3.7-2
- Added support for timestamps
- Another way to treat CFLAGS

* Wed Jan 31 2006 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 1.3.7-1
- Initial package.
