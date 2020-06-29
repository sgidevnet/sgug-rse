%{?python_enable_dependency_generator}
%global srcname animatplot

Name:           python-%{srcname}
Version:        0.4.1
Release:        7%{?dist}
Summary:        Making animating in Matplotlib easy

License:        MIT
URL:            https://github.com/t-makaro/animatplot
# PyPI tarball does not contain docs and tests.
Source0:        https://github.com/t-makaro/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%description
A Python package for making interactive animated plots build on Matplotlib.


%package -n     python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

BuildRequires:  pandoc
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sphinx) >= 1.5.1
BuildRequires:  python3dist(sphinx-rtd-theme)
BuildRequires:  python3dist(ipykernel)
BuildRequires:  python3dist(nbsphinx)
BuildRequires:  python3dist(matplotlib) >= 2.2
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(pillow)
BuildRequires:  python3dist(pytest)

%description -n python3-%{srcname}
A Python package for making interactive animated plots build on Matplotlib.


%package -n     python3-%{srcname}-doc
Summary:        Documentation for python3-%{srcname}

%description -n python3-%{srcname}-doc
Documentation for python3-%{srcname}.


%prep
%autosetup -n %{srcname}-%{version} -p1

# Remove bundled egg-info
rm -rf %{srcname}.egg-info


%build
%py3_build

pushd docs
%{__python3} -m sphinx source html
# remove the sphinx-build leftovers
rm -rf html/.{buildinfo,doctrees}
popd


%install
%py3_install


%check
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=%{buildroot}%{python3_sitelib} \
    pytest-3


%files -n python3-%{srcname}
%doc README.md
%license LICENSE
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-%{version}-py?.?.egg-info

%files -n python3-%{srcname}-doc
%doc docs/html


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.4.1-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.1-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.1-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Mar 15 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.4.1-2
- Add explicit sphinx_rtd_theme BuildRequires

* Tue Mar 05 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.4.1-1
- Update to latest version

* Sat Feb 23 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.4.0-1
- Update to latest version

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 15 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.0-2
- Enable python dependency generator

* Sat Jan 12 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3.0-1
- Update to latest version

* Fri Aug 10 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.2-2
- Fix license file listing

* Wed Aug 08 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.2-1
- Initial package.
