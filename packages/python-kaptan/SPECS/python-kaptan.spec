%global srcname kaptan

Name:           python-%{srcname}
Version:        0.5.12
Release:        6%{?dist}
Summary:        Configuration parser

License:        BSD
URL:            https://pypi.python.org/pypi/kaptan
Source:         https://github.com/emre/kaptan/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%description
%{summary}.

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  (python3dist(pyyaml) >= 3.13 with python3dist(pyyaml) < 6)
BuildRequires:  python3dist(pytest) >= 4.4.1
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{summary}.

%prep
%autosetup -n %{srcname}-%{version}
# https://github.com/emre/kaptan/pull/163
sed -i -e 's/==/>=/' requirements/test.txt

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

# A man page has been requested upstream here:
# https://github.com/emre/kaptan/issues/44
%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{srcname}-*.egg-info/
%{python3_sitelib}/%{srcname}/
%{_bindir}/%{srcname}

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.5.12-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.12-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.12-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat May 11 11:38:45 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.12-1
- Update to 0.5.12

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Sep 18 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 0.5.5-7
- Drop python2-kaptan (#1630280).

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.5.5-5
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Dec 17 2016 David Roble <robled@electronsweatshop.com> 0.5.5-1
- Initial release
