%global srcname dict-sorted
%global modname sdict
%global eggname %(n=%{srcname}; echo ${n//-/.})

Name:           python-%{srcname}
Version:        1.0.0
Release:        16%{?dist}
Summary:        Dictionaries sorted by key or by comparison function

License:        BSD
URL:            https://github.com/lukesneeringer/dict-sorted
Source0:        %{url}/archive/releases/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%description
%{summary}.

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3dist(six) >= 1.3

%description -n python3-%{srcname}
%{summary}.

Python 3 version.

%package doc
Summary:        Documentation for %{name}
BuildRequires:  %{_bindir}/sphinx-build

%description doc
%{summary}.

%prep
%autosetup -n %{srcname}-releases-%{version}

%build
%py3_build
sphinx-build -W -b html -d docs/_build/.doctrees/ docs/ docs/_build/html/

%install
%py3_install
rm -f docs/_build/html/.buildinfo

%check
%{__python3} test.py -v

%files -n python3-%{srcname}
%license LICENSE
%{python3_sitelib}/%{eggname}-*.egg-info/
%{python3_sitelib}/%{modname}/

%files doc
%license LICENSE
%doc docs/_build/html

%changelog
* Mon May 25 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-16
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-14
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Sun Aug 18 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-13
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-10
- Subpackage python2-dict-sorted has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Wed Dec 26 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.0-9
- Enable python dependency generator

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-7
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 29 2017 Igor Gnatenko <ignatenko@redhat.com> - 1.0.0-4
- Switch to bin/sphinx-build

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-2
- Rebuild for Python 3.6

* Fri Aug 26 2016 Igor Gnatenko - 1.0.0-1
- Initial package
