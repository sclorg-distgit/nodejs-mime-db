%{?scl:%scl_package nodejs-mime-db}
%{!?scl:%global pkg_name %{name}}
%global npm_name mime-db

%{!?scl:%global enable_tests 0}

%{?nodejs_find_provides_and_requires}

Name:		%{?scl_prefix}nodejs-mime-db
Version:	1.15.0
Release:	4%{?dist}
Summary:	Media Type Database
Url:		https://github.com/jshttp/mime-db
Source0:	https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
License:	MIT

BuildArch:	noarch
ExclusiveArch:	%{ix86} x86_64 %{arm} noarch

BuildRequires:	%{?scl_prefix}nodejs-devel

%if 0%{?enable_tests}
BuildRequires:	npm(bluebird)
BuildRequires:	npm(co)
BuildRequires:	npm(cogent)
BuildRequires:	npm(csv-parse)
BuildRequires:	npm(gnode)
BuildRequires:	npm(istanbul)
BuildRequires:	npm(mocha)
BuildRequires:	npm(raw-body)
BuildRequires:	npm(stream-to-array)
%endif

%description
Media Type Database

%prep
%setup -q -n package

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}

cp -pr db.json package.json index.js \
	%{buildroot}%{nodejs_sitelib}/%{npm_name}

%{nodejs_symlink_deps}

%if 0%{?enable_tests}
%check
%{nodejs_symlink_deps} --check
mocha --reporter spec --bail --check-leaks test/
%endif

%files
%{nodejs_sitelib}/mime-db

%doc README.md
%doc LICENSE

%changelog
* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.15.0-4
- rebuilt

* Tue Sep 22 2015 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.15.0-3
- Add missing files to %%install

* Mon Jul 20 2015 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.15.0-2
- Correct variable

* Mon Jul 20 2015 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.15.0-1
- Initial build
