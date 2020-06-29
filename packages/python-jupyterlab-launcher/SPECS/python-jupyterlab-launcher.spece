Name:           python-jupyterlab-launcher
Version:        0.13.1
Release:        2%{?dist}
Summary:        JupyterLab Launcher

License:        BSD
URL:            http://jupyter.org
Source0:        %pypi_source jupyterlab_launcher
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(jsonschema) >= 2.6
BuildRequires:  python3dist(mock)
BuildRequires:  python3dist(notebook) >= 4.2
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(setuptools)

%?python_enable_dependency_generator

%description
This package is used to launch an application built using JupyterLab.

%package -n     python3-jupyterlab-launcher
Summary:        %{summary}
%{?python_provide:%python_provide python3-jupyterlab-launcher}

%description -n python3-jupyterlab-launcher
This package is used to launch an application built using JupyterLab.


%prep
%autosetup -n jupyterlab_launcher-%{version}

%build
%py3_build

%install
%py3_install

%check
%{__python3} -m pytest -vv

%files -n python3-jupyterlab-launcher
%license LICENSE
%doc README.md
%{python3_sitelib}/jupyterlab_launcher
%{python3_sitelib}/jupyterlab_launcher-%{version}-py?.?.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.13.1-2
- Rebuilt for Python 3.9

* Tue Mar 10 2020 Tomas Hrnciar <thrnciar@redhat.com> - 0.13.1-1
- Update to 0.13.1

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.11.0-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.11.0-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Miro Hrončok <mhroncok@redhat.com> - 0.11.0-1
- Update to 0.11.0

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.10.4-2
- Rebuilt for Python 3.7

* Tue Feb 20 2018 Miro Hrončok <mhroncok@redhat.com> - 0.10.4-1
- Initial package
