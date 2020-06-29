%{?!_without_python2:%global with_python2 0%{?_with_python2:1} || !(0%{?fedora} >= 30 || 0%{?rhel} >= 8)}
%{?!_without_python3:%global with_python3 0%{?_with_python3:1} || !0%{?rhel} || 0%{?rhel} >= 7}

%global srcname bitstring

Name:           python-%{srcname}
Version:        3.1.7
Release:        2%{?dist}
Summary:        Simple construction, analysis and modification of binary data

License:        MIT
URL:            https://github.com/scott-griffiths/%{srcname}
Source0:        https://github.com/scott-griffiths/%{srcname}/archive/%{srcname}-%{version}/%{srcname}-%{srcname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  dos2unix

%description
bitstring is a pure Python module designed to help make the creation and
analysis of binary data as simple and natural as possible.

Bitstrings can be constructed from integers (big and little endian), hex,
octal, binary, strings or files. They can be sliced, joined, reversed,
inserted into, overwritten, etc. with simple functions or slice notation.
They can also be read from, searched and replaced, and navigated in, similar
to a file or stream.


%if 0%{?with_python2}
%package -n python2-%{srcname}
Summary:        %{summary}
BuildRequires:  python2-devel
BuildRequires:  python2-nose
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname}
bitstring is a pure Python module designed to help make the creation and
analysis of binary data as simple and natural as possible.

Bitstrings can be constructed from integers (big and little endian), hex,
octal, binary, strings or files. They can be sliced, joined, reversed,
inserted into, overwritten, etc. with simple functions or slice notation.
They can also be read from, searched and replaced, and navigated in, similar
to a file or stream.
%endif


%if 0%{?with_python3}
%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-nose
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%description -n python%{python3_pkgversion}-%{srcname}
bitstring is a pure Python module designed to help make the creation and
analysis of binary data as simple and natural as possible.

Bitstrings can be constructed from integers (big and little endian), hex,
octal, binary, strings or files. They can be sliced, joined, reversed,
inserted into, overwritten, etc. with simple functions or slice notation.
They can also be read from, searched and replaced, and navigated in, similar
to a file or stream.
%endif


%prep
%autosetup -n %{srcname}-%{srcname}-%{version}

dos2unix README.rst release_notes.txt
sed -i '1{s|^#!/usr/bin/env python||}' %{srcname}.py


%build
%if 0%{?with_python2}
%py2_build
%endif

%if 0%{?with_python3}
%py3_build
%endif


%install
%if 0%{?with_python2}
%py2_install
%endif

%if 0%{?with_python3}
%py3_install
%endif


%check
%if 0%{?with_python2}
%{__python2} -m nose -w test
%endif

%if 0%{?with_python3}
%{__python3} -m nose -w test
%endif


%if 0%{?with_python2}
%files -n python2-%{srcname}
%license LICENSE
%doc README.rst release_notes.txt
%{python2_sitelib}/%{srcname}.py
%{python2_sitelib}/%{srcname}.py[co]
%{python2_sitelib}/%{srcname}-%{version}-py%{python2_version}.egg-info
%endif

%if 0%{?with_python3}
%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE
%doc README.rst release_notes.txt
%{python3_sitelib}/%{srcname}.py
%{python3_sitelib}/__pycache__/%{srcname}.cpython-%{python3_version_nodots}*.pyc
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info
%endif


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.1.7-2
- Rebuilt for Python 3.9

* Sun May 10 2020 Scott K Logan <logans@cottsay.net> - 3.1.7-1
- Update to 3.1.7 (rhbz#1831898)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 3.1.6-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.1.6-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 09 2019 Scott K Logan <logans@cottsay.net> - 3.1.6-1
- Update to 3.1.6
- Introduce Python 3 subpackage in EPEL

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 17 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.1.5-7
- Subpackage python2-bitstring has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.1.5-5
- Rebuilt for Python 3.7

* Sun Feb 11 2018 Iryna Shcherbina <ishcherb@redhat.com> - 3.1.5-4
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun May 21 2017 Scott K Logan <logans@cottsay.net> - 3.1.5-1
- Update to 3.1.5
- Include LICENSE file

* Tue Apr 26 2016 Scott K Logan <logans@cottsay.net> - 3.1.4-1
- Initial package
