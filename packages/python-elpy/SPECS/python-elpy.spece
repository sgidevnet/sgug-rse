%global pypi_name elpy
%global desc %{expand: \
The Emacs Lisp Python Environment.Elpy is a mode for Emacs to support writing
Python code. This package provides the backend within Python to support auto-
completion, documentation extraction, and navigation.Emacs will start the
protocol by running the module itself, like so: python -m elpyThis will emit a
greeting string on a single line, and then wait for the protocol to start.
Details of...}

Name:           python-%{pypi_name}
Version:        1.34.0
Release:        1%{?dist}
Summary:        Backend for the elpy Emacs mode

License:        GPLv3
URL:            https://github.com/jorgenschaefer/elpy
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%{?python_enable_dependency_generator}

BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: %{py3_dist nose}
BuildRequires: %{py3_dist flake8} >= 2
BuildRequires: %{py3_dist setuptools} 
BuildRequires: bumpversion
BuildRequires: %{py3_dist coverage}
BuildRequires: %{py3_dist mock}
BuildRequires: %{py3_dist twine}
BuildRequires: %{py3_dist wheel}
BuildRequires: %{py3_dist jedi}
BuildRequires: %{py3_dist autopep8}
BuildRequires: %{py3_dist black}
BuildRequires: %{py3_dist rope}
BuildRequires: %{py3_dist yapf}
BuildRequires: %{py3_dist multidict}
BuildRequires: %{py3_dist appdirs}
BuildRequires: %{py3_dist regex}
BuildRequires: %{py3_dist pathspec}
BuildRequires: %{py3_dist attrs}
BuildRequires: %{py3_dist click}
BuildRequires: %{py3_dist toml}
BuildRequires: %{py3_dist typed-ast}

%description
%{desc}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%{desc}

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

find . -type f -name "*.py" -exec sed -i '/^#![  ]*\/usr\/bin\/env.*$/ d' {} ';'

%build
%py3_build

%install
%py3_install

#%check
#%{__python3} setup.py test

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Wed Jun 03 2020 Luis Bazan <lbazan@fedoraproject.org> - 1.34.0-1
- New upstream version

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.29.1-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.29.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.29.1-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.29.1-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.29.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 17 2019 Luis Bazan <lbazan@fedoraproject.org> - 1.29.1-1
- Fix comments of review

* Thu Mar 21 2019 Luis Bazan <lbazan@fedoraproject.org> - 1.28.0-1
- Initial package.
