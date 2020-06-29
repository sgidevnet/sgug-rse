%{?python_enable_dependency_generator}
%global srcname citeproc-py

Name:           python-%{srcname}
Version:        0.5.1
Release:        2%{?dist}
Summary:        Citations and bibliography formatter

License:        BSD
URL:            https://pypi.python.org/pypi/citeproc-py
Source0:        %{pypi_source}

BuildArch:      noarch

%description
%{summary}.

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3dist(rnc2rng) >= 2.2
BuildRequires:  python3dist(lxml)

%description -n python3-%{srcname}
%{summary}.

Python 3 version.

%prep
%autosetup -n %{srcname}-%{version}
rm -vrf *.egg-info

%build
%py3_build

%install
%py3_install

sed -i -e '1s|^.*$|#!%{__python3}|' %{buildroot}%{_bindir}/csl_unsorted

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst examples
%{python3_sitelib}/citeproc/
%{python3_sitelib}/citeproc_py*.egg-info/

%{_bindir}/csl_unsorted

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.5.1-2
- Rebuilt for Python 3.9

* Tue Apr 21 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.5.1-1
- Update to 0.5.1

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.0-10
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.0-9
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Dec 24 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.0-6
- Enable python dependency generator

* Wed Oct 17 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.4.0-5
- Subpackage python2-citeproc-py has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.4.0-3
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 03 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.0-1
- Update to 0.4.0

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.3.0-5
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Nov 25 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.3.0-2
- Only one version of binary

* Wed Nov 11 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.3.0-1
- Initial package
