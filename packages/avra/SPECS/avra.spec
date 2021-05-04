Name:		avra
Version:	1.3.0
Release:	12%{?dist}
Summary:	Atmel AVR assembler

License:	GPLv2+
URL:		http://avra.sourceforge.net/
Source0:	http://downloads.sourceforge.net/avra/%{name}-%{version}.tar.bz2
BuildRequires:  gcc
BuildRequires:	autoconf
BuildRequires:	automake

%description
Avra is an assembler for Atmel's AVR 8-bit RISC microcontollers.
It is mostly compatible with Atmel's own assembler, but provides new features
such as better macro support and additional preprocessor directives.
This package also contains various device definition files.


%prep
%setup -q

#ugly hack to build avra, FIXME in future versions
mv src/* .
aclocal
autoconf
touch ChangeLog NEWS
automake -a
autoreconf -vif


%build
%configure
make %{?_smp_mflags}


%install
make install INSTALL="%{_bindir}/install -p" DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{name}/
install -p -m 0644 includes/*.inc $RPM_BUILD_ROOT/%{_datadir}/%{name}/


%files
%doc AUTHORS TODO README COPYING doc/ examples/
%{_datadir}/%{name}
%{_bindir}/%{name}


%changelog
* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Jun 03 2014 Filipe Rosset <rosset.filipe@gmail.com> - 1.3.0-1
- Rebuilt for latest upstream release, spec cleanup, fixes rhbz #768896

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Sep 29 2009 Alex Musolino <musolinoa@gmail.com> - 1.2.3-4
- Pass `install` arguments to make via command line arguments

* Fri Sep 25 2009 Alex Musolino <musolinoa@gmail.com> - 1.2.3-3
- Moved build preperation commands to %%prep section
- Retain timestamps throughout
- Mentioned device definitions in %%description

* Sun Sep 20 2009 Alex Musolino <musolinoa@gmail.com> - 1.2.3-2
- Added examples
- Added include files

* Sat Sep 19 2009 Alex Musolino <musolinoa@gmail.com> - 1.2.3-1
- Initial RPM package
