%global srcname tftpy

Name:		python-%{srcname}
Version:	0.8.0
Release:	6%{?dist}
Summary:	TFTPy is a pure Python implementation of the Trivial FTP protocol

License:	MIT
URL:		https://github.com/msoulier/%{srcname}
Source0:	%{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:	noarch


%global _description\
Tftpy is a TFTP library for the Python programming language. It includes\
client and server classes, with sample implementations. Hooks are included\
for easy inclusion in a UI for populating progress indicators. It supports\
RFCs 1350, 2347, 2348 and the tsize option from RFC 2349.\


%description %_description

%if 0%{?fedora} <= 31
%package -n python2-%{srcname}
Summary: %summary
%{?python_provide:%python_provide python2-%{srcname}}

BuildRequires:	python2-devel, python2-setuptools

%description -n python2-%{srcname} %_description
%endif

%package -n python3-%{srcname}
Summary: %summary
%{?python_provide:%python_provide python3-%{srcname}}

BuildRequires:	python3-devel, python3-setuptools
Conflicts:	python2-%{srcname} <= 0.8.0-1

%description -n python3-%{srcname} %_description


%prep
%setup -q -n %{srcname}-%{version}


%build
%if 0%{?fedora} <= 31
%py2_build
%endif
%py3_build


%install
%if 0%{?fedora} <= 31
%py2_install
# rename python2 commands to avoid file conflicts with python3 package
mv ${RPM_BUILD_ROOT}%{_bindir}/tftpy_client{,2}.py
mv ${RPM_BUILD_ROOT}%{_bindir}/tftpy_server{,2}.py
%endif

%py3_install

%if 0%{?fedora} <= 31
# rename python3 commands to avoid file conflicts with python2 package
mv ${RPM_BUILD_ROOT}%{_bindir}/tftpy_client{,3}.py
mv ${RPM_BUILD_ROOT}%{_bindir}/tftpy_server{,3}.py
# make python3 commands the default version (TODO: use alternatives)
ln -s tftpy_client3.py ${RPM_BUILD_ROOT}%{_bindir}/tftpy_client.py
ln -s tftpy_server3.py ${RPM_BUILD_ROOT}%{_bindir}/tftpy_server.py
%endif


%if 0%{?fedora} <= 31
%files -n python2-%{srcname}
%doc README COPYING
%{_bindir}/tftpy_client2.py
%{_bindir}/tftpy_server2.py
%{python2_sitelib}/tftpy/
%{python2_sitelib}/*.egg-info
%endif


%files -n python3-%{srcname}
%doc README COPYING
%if 0%{?fedora} <= 31
%{_bindir}/tftpy_client3.py
%{_bindir}/tftpy_server3.py
%endif
%{_bindir}/tftpy_client.py
%{_bindir}/tftpy_server.py
%{python3_sitelib}/tftpy/
%{python3_sitelib}/*.egg-info


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.8.0-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8.0-3
- Rebuilt for Python 3.8

* Wed Aug 14 2019 Jeff Bastian <jbastian@redhat.com> - 0.8.0-2
- Stop building python2-tftpy for rawhide (Fedora 32)
- Fixes rhbz #1738085

* Tue Aug 13 2019 Jeff Bastian <jbastian@redhat.com> - 0.8.0-1
- Update to upstream version 0.8.0 for Python 3.x support
- Added python3-tftpy binary package
- Fixes rhbz #1738085

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.6.2-6
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.6.2-4
- Python 2 binary package renamed to python2-tftpy
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Dec 03 2016 Filipe Rosset <rosset.filipe@gmail.com> - 0.6.2-1
- Rebuilt for new upstream release 0.6.2, fixes rhbz #1166406

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Oct 16 2013 Jeff Bastian <jbastian@redhat.com> - 0.6.1-1
- upstream update to v0.6.1

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Mar  8 2013 Jeff Bastian <jbastian@redhat.com> - 0.6.0-1
- initial release of tftpy as an rpm for Fedora 18
