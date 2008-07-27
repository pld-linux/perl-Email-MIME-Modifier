#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Email
%define	pnam	MIME-Modifier
Summary:	Email::MIME::Modifier - modify Email::MIME objects easily
Summary(pl.UTF-8):	Email::MIME::Modifier - łatwe modyfikowanie obiektów Email::MIME
Name:		perl-Email-MIME-Modifier
Version:	1.442
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e5781783dfd0d4d63ea77990fc6dcff6
URL:		http://search.cpan.org/dist/Email-MIME-Modifier/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Email-MIME >= 1.7
BuildRequires:	perl-Email-MIME-ContentType >= 1
BuildRequires:	perl-Email-MIME-Encodings >= 1.2
BuildRequires:	perl-Email-MessageID >= 1.2
BuildRequires:	perl-Email-Simple >= 1.9
%endif
# not autodetected
Requires:	perl-Email-MIME >= 1.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides a number of useful methods for manipulating MIME messages.

%description -l pl.UTF-8
Pakiet dostarcza wiele użytecznych metod do obróbki wiadomości MIME.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Email/MIME/*.pm
%{_mandir}/man3/*
