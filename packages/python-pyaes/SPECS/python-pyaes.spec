%global srcname pyaes


Name:		python-%{srcname}
Version:	1.6.1
Release:	3%{?dist}
Summary:	Pure-Python implementation of AES block-cipher and common modes of operation
License:	MIT
URL:		https://github.com/ricmoo/%{srcname}
Source0:	https://github.com/ricmoo/%{srcname}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch1:		python-pyaes-0001-Use-relative-imports-during-tests.patch
BuildArch:      noarch


%description
A pure-Python implementation of the AES block cipher algorithm and the common
modes of operation (CBC, CFB, CTR, ECB and OFB).


%package -n python3-%{srcname}
Summary:	%{summary}
BuildRequires:  python3-crypto
BuildRequires:  python3-devel
%{?python_provide:%python_provide python3-%{srcname}}


%description -n python3-%{srcname}
A pure-Python implementation of the AES block cipher algorithm and the common
modes of operation (CBC, CFB, CTR, ECB and OFB).


%prep
%autosetup -p1 -n %{srcname}-%{version}


%build
%py3_build


%install
%py3_install


%check
%{__python3} tests/test-aes.py
%{__python3} tests/test-blockfeeder.py
%{__python3} tests/test-util.py


%files -n python3-%{srcname}
%license LICENSE.txt
%doc README.md
%{python3_sitelib}/*


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.6.1-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 13 2019 Peter Lemenkov <lemenkov@gmail.com> - 1.6.1-1
- Ver. 1.6.1

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.6.0-10
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.6.0-9
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Sep 20 2018 Peter Lemenkov <lemenkov@gmail.com> - 1.6.0-6
- Remove python2 subpackage

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.6.0-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Mar 31 2017 Peter Lemenkov <lemenkov@gmail.com> - 1.6.0-1
- Initial build
