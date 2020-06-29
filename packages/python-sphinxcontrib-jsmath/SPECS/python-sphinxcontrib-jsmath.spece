%global pypi_name sphinxcontrib-jsmath

# when bootstrapping sphinx, we cannot run tests yet
%bcond_without check

Name:           python-%{pypi_name}
Version:        1.0.1
Release:        8%{?dist}
Summary:        Sphinx extension for math in HTML via JavaScript
License:        BSD
URL:            http://sphinx-doc.org/
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%if %{with check}
BuildRequires:  python3-pytest
BuildRequires:  python3-sphinx >= 1:2
%endif

%description
sphinxcontrib-jsmath is a sphinx extension which renders display math in HTML
via JavaScript.


%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
sphinxcontrib-jsmath is a sphinx extension which renders display math in HTML
via JavaScript.


%prep
%autosetup -n %{pypi_name}-%{version}


%build
%py3_build


%install
%py3_install


%if %{with check}
%check
%{__python3} -m pytest
%endif


%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/sphinxcontrib/
%{python3_sitelib}/sphinxcontrib_jsmath-%{version}-py%{python3_version}-*.pth
%{python3_sitelib}/sphinxcontrib_jsmath-%{version}-py%{python3_version}.egg-info/


%changelog
* Sat May 23 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-8
- Rebuilt for Python 3.9

* Fri May 22 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-7
- Bootstrap for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Fri Aug 16 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-4
- Rebuilt for Python 3.8

* Thu Aug 15 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-3
- Bootstrap for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Mar 01 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-1
- Initial package
