%global pypi_name asciitree

Name:       python-%{pypi_name}
Version:    0.3.3
Release:    16%{?dist}
Summary:    Draws ASCII trees

License:    MIT
URL:        https://github.com/mbr/asciitree
Source0:    https://github.com/mbr/asciitree/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:  noarch

%description
Sometimes you just want to draw ascii trees in your terminal.

Read the documentation at http://pythonhosted.org/asciitree

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Sometimes you just want to draw ascii trees in your terminal.

Read the documentation at http://pythonhosted.org/asciitree

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

# Need fixing by upstream
#%check
#PYTHONPATH=%{buildroot}/%{python3_sitelib} %{__python3} -v -m unittest discover %{pypi_name}

%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}*

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.3.3-16
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 09 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.3-14
- Update spec file
- Tests
- Use upstream source

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.3-13
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 17 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.3.3-10
- Subpackage python2-asciitree has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.3.3-8
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.3.3-4
- Rebuild for Python 3.6

* Wed Oct 05 2016 Ralph Bean <rbean@redhat.com> - 0.3.3-3
- Whoops, got that backwards.

* Wed Oct 05 2016 Ralph Bean <rbean@redhat.com> - 0.3.3-2
- Conditionalize requirements for el7.

* Tue Sep 13 2016 Ralph Bean <rbean@redhat.com> - 0.3.3-1
- Initial package for Fedora
