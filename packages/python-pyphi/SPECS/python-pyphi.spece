# Note: package is python 3 only
%global srcname pyphi

%bcond_without tests

%global _description %{expand:
PyPhi is a Python library for computing integrated information, and the
associated quantities and objects.

If you use this code, please cite the manuscript:

Mayner WGP, Marshall W, Albantakis L, Findlay G, Marchman R, Tononi G (2017).
PyPhi: A toolbox for integrated information. arXiv:1712.09644 [q-bio.NC].

The manuscript is available at https://arxiv.org/abs/1712.09644.}

%{?python_enable_dependency_generator}

Name:           python-%{srcname}
Version:        1.2.0
Release:        6%{?dist}
Summary:        A library for computing integrated information

License:        GPLv3
URL:            %{pypi_url}
Source0:        https://github.com/wmayner/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
# To build docs, and run tests
BuildRequires:  %{py3_dist asv}
BuildRequires:  %{py3_dist decorator}
BuildRequires:  %{py3_dist joblib}
BuildRequires:  %{py3_dist numpy}
BuildRequires:  %{py3_dist psutil}
BuildRequires:  %{py3_dist pyemd}
BuildRequires:  %{py3_dist pymongo}
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist pytest-lazy-fixture}
BuildRequires:  %{py3_dist pyyaml}
BuildRequires:  %{py3_dist redis}
BuildRequires:  %{py3_dist scipy}
BuildRequires:  %{py3_dist sphinx}
BuildRequires:  %{py3_dist sphinx_rtd_theme}
BuildRequires:  %{py3_dist setuptools}
BuildRequires:  %{py3_dist tblib}
BuildRequires:  %{py3_dist tqdm}
BuildRequires:  %{py3_dist wheel}

%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname} %_description

%package doc
Summary:        %{summary}

%description doc
Documentation for %{name}


%prep
%autosetup -n %{srcname}-%{version}

# sphinx 1.3+, it's an extension
# Also sent upstream: https://github.com/wmayner/pyphi/pull/22
sed -i "s/sphinxcontrib.napoleon/sphinx.ext.napoleon/" docs/conf.py

find pyphi -name "*.py" -exec sed -i '/#!\/usr\/bin\/env python3/ d' '{}' \;

%build
%py3_build

make -C docs SPHINXBUILD=sphinx-build-3 html
rm docs/_build/html/{.doctrees,.buildinfo} -vf

%install
%py3_install

%check
%if %{with tests}
py.test-%{python3_version}
%endif

%files -n python3-%{srcname}
%license LICENSE.md
%doc README.md CHANGELOG.md CACHING.rst redis.conf
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-%{version}-py3.?.egg-info

%files doc
%license LICENSE.md
%doc docs/_build/html/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.2.0-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.0-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 12 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.2.0-2
- Enable tests

* Sat Jun 22 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.2.0-1
- Update to 1.2.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 19 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.1.0-2
- Update license
- Fix doc generation
- Correct rpmlint errors

* Wed Nov 14 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.1.0-1
- Initial rpm build
