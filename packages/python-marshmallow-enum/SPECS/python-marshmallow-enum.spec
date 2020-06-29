%global modname marshmallow_enum
%global pypi_name marshmallow-enum
%global _docdir_fmt %{name}

Name:           python-%{pypi_name}
Version:        1.5.1
Release:        3%{?dist}
Summary:        Enum serializer/deserializer for use with Marshmallow

License:        MIT
URL:            https://github.com/justanr/marshmallow_enum
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch

%description
A Python enum serializer/deserializer for use with Marshmallow.

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

BuildRequires:  python3-pytest
BuildRequires:  python3-marshmallow
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
A Python enum serializer/deserializer for use with Marshmallow.

%prep
%autosetup -n %{modname}-%{version}
rm -vf tox.ini

%build
%py3_build

%install
%py3_install

%check
PYTHONPATH=%{buildroot}/%{python3_sitelib} py.test-%{python3_version} -v

%files -n python3-%{pypi_name}
%doc README.md CHANGELOG
%license LICENSE
%{python3_sitelib}/%{modname}/
%{python3_sitelib}/%{modname}-*.egg-info/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.5.1-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 09 2019 Fabian Affolter <mail@fabian-affolter.ch> - 1.5.1-1
- Update to latest upstream release 1.5.1
- Update spec file

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.4.1-8
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 17 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.4.1-5
- Subpackage python2-marshmallow-enum has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.4.1-3
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Nov 08 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.4.1-1
- Update to 1.4.1

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.0-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Jul 07 2016 Igor Gnatenko <ignatenko@redhat.com> - 1.0-1
- Initial package
