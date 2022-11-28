Name:		wsl
Version:	0.2.2
Release:	12%{?dist}
Summary:	Wsman Shell Command Line "whistle"

License:	BSD
URL:		http://linux.dell.com/files/%{name}
Source0:	http://linux.dell.com/files/%{name}/%{name}-%{version}.tar.gz

Requires:	bash curl libxml2
Requires:	gpg
BuildArch:	noarch

%description
WSL (aka "whistle") contains various scripts that serve as a client interface 
to WSMAN or Web Services for Management protocol base on DMTF standard 
specification. WSMAN provides standards based messaging for systems management 
CIM-style objects.



%prep
%setup -q

%build


%install

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/%{name}
install -m 644 %{_builddir}/%{name}-%{version}/wsl-functions $RPM_BUILD_ROOT/%{_sysconfdir}/%{name}
install -m 644 %{_builddir}/%{name}-%{version}/wsl-ws2textc.xsl $RPM_BUILD_ROOT/%{_sysconfdir}/%{name}


mkdir -p $RPM_BUILD_ROOT/%{_bindir}
install -m 755 %{_builddir}/%{name}-%{version}/viwsl $RPM_BUILD_ROOT/%{_bindir}
install -m 755 %{_builddir}/%{name}-%{version}/wsl $RPM_BUILD_ROOT/%{_bindir}
install -m 755 %{_builddir}/%{name}-%{version}/wslcred $RPM_BUILD_ROOT/%{_bindir}
install -m 755 %{_builddir}/%{name}-%{version}/wslecn $RPM_BUILD_ROOT/%{_bindir}
install -m 755 %{_builddir}/%{name}-%{version}/wslenum $RPM_BUILD_ROOT/%{_bindir}
install -m 755 %{_builddir}/%{name}-%{version}/wslget $RPM_BUILD_ROOT/%{_bindir}
install -m 755 %{_builddir}/%{name}-%{version}/wslid $RPM_BUILD_ROOT/%{_bindir}
install -m 755 %{_builddir}/%{name}-%{version}/wslinvoke $RPM_BUILD_ROOT/%{_bindir}
install -m 755 %{_builddir}/%{name}-%{version}/wslput $RPM_BUILD_ROOT/%{_bindir}
install -m 755 %{_builddir}/%{name}-%{version}/wxmlgetvalue $RPM_BUILD_ROOT/%{_bindir}



mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
install -m 644 %{_builddir}/%{name}-%{version}/wsl.1 $RPM_BUILD_ROOT%{_mandir}/man1




%files
%{_bindir}/*
%{_sysconfdir}/%{name}


%doc LICENSE README-wsl VERSION wslrc
%{_mandir}/man1/%{name}.1.*




%changelog
* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Nov  6 2012 Chris Poblete <chris_poblete@dell.com> - 0.2.2-1
- Added viwsl to spec file

* Fri Nov  2 2012 Praveen K Paladugu <praveen_paladugu@dell.com> - 0.2.0-1
- Using curl in place of wget to talk to remote server.

* Mon Oct  8 2012 Praveen K Paladugu <praveen_paladugu@dell.com> - 0.1.8-2
- Removing the explicit installation of the doc files as the %%doc macro will handle the same
- Not zipping the man file, as the package build will handle it.

* Mon Oct  8 2012 Praveen K Paladugu <praveen_paladugu@dell.com>- 0.1.8-1
- Minor changes to spec file, following Fedora reviewer's suggestions.


* Tue Oct  2 2012 Chris Poblete <chris_poblete@dell.com> - 0.1.7c-1
- Added a man page for wsl

* Tue Sep 25 2012 Chris Poblete <chris_poblete@dell.com> - 0.1.0-1
- initial version of WSL.

